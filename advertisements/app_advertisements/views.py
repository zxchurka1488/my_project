from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Advertisement , User
from .forms import AdvertisementForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.db.models import Count


def index(request):
    title = request.GET.get('query')
    if title:
        advertisements = Advertisement.objects.filter(title__contains = title)
    else:
        advertisements = Advertisement.objects.all()
    context = {"advertisements": advertisements,
               "title" : title
               }
    return render(request, 'app_advertisements/index.html', context)
def top_sellers(request):
    users = User.objects.annotate(adv_count=Count('advertisement')).order_by('-adv_count')
    context = {'users' : users}
    return render(request, 'app_advertisements/top-sellers.html', context)

@login_required(login_url=reverse_lazy('login'))
def advertisement_post(request):
    if request.method == "POST":
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            advertisement = Advertisement(**form.cleaned_data)
            advertisement.user = request.user
            advertisement.save()
            url = reverse('index')
            return redirect(url)
    else:
        form = AdvertisementForm()
    context = {'form': form}
    return render(request, 'app_advertisements/advertisement-post.html', context)

def advertisement_detail(request, pk):
    advertisement = Advertisement.objects.get(id = pk)

    context = {"adv":advertisement}
    return render(request, 'app_advertisements/advertisement.html', context)