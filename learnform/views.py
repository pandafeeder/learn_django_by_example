from django import forms
from django.views.generic import TemplateView
from django.shortcuts import render

class LoginForm(forms.Form):
    #this field will get a label tage with the same word as field but first char capitalized
    #and underscore replaced with space
    your_name= forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())


def login(request):
    form = LoginForm()
    return render(request, 'learnform/index_form.html', {'form': form})


def welcome(request):
    pass
