from django import forms
from django.forms import ModelForm

from .models import Ad


class NewAd(forms.Form):
    advertiser_id = forms.IntegerField()
    title = forms.CharField(max_length=40)
    image = forms.ImageField()
    link = forms.CharField(max_length=512)


# class NewAd(ModelForm):
#     class Meta:
#         model = Ad
#         fields = ['title', 'link', 'img']
