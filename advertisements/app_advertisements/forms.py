from django.forms import ModelForm, TextInput, Textarea, NumberInput, CheckboxInput, FileInput
from .models import Advertisement
from django.core.exceptions import ValidationError
class AdvertisementForm(ModelForm):
    def clean_title(self):
        data = self.cleaned_data['title']
        if data[0] == '?':
            raise ValidationError('Заголовок не может начинатся с "?".')
        return data

    class Meta:
        model = Advertisement
        fields = [ 'title', 'description', 'price', 'auction', 'image']
        widgets = { 'title': TextInput(attrs={'class': 'form-control form-control-lg'}),
                    'description' : Textarea(attrs={'class': 'form-control form-control-lg'}),
                    'price' : NumberInput(attrs={'class': 'form-control form-control-lg'}),
                    'auction' : CheckboxInput(attrs={'class': 'form-check-input'}),
                    'image' : FileInput(attrs={'class': 'form-control form-control-lg'})
                     }


"""
class AdvertisementForm(forms.Form):
    title = forms.CharField(max_length=64, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control form-control-lg'}))
    price = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control form-control-lg'}))
    auction = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control form-control-lg'}))
"""