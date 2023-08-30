from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from  django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, DetailView, CreateView
from .forms import RegisterUserForm, User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from .models import User
@login_required(login_url= reverse_lazy('login'))
def profile_view(request):
    return render(request, 'app_auth/profile.html')

def login_view(request):
    redirect_url = reverse('profile')
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect(redirect_url)
        else:
            return render(request, 'app_auth/login.html')
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect(redirect_url)
    return render(request, 'app_auth/login.html', {'error': 'Пользователь не найден.'})

def logout_view(request):
    logout(request)
    return redirect(reverse('login'))

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'app_auth/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super(RegisterUser, self).get_context_data(**kwargs)
        return context

""""
def auth_post(request):

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = User(**form.cleaned_data)
            user.save()
            url = reverse('index')
            return redirect(url)

    else:
        form = ()
    context = {'form': form}
    return render(request, 'app_auth/register.html', context)


def register_view(request):
    if request.POST == 'POST':
        form = UserCreationForm()
        if form.is_valid():
            form.save()
            url = reverse('index')
            return redirect(url)
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'app_auth/register.html', context)

"""
