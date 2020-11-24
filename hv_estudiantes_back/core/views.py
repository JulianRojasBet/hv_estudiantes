from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import Oferta
from .serializers import OfertaSerializer

from django.http import HttpResponse

from core.forms import SignUpForm, SignUpOfferForm, AddNewOfferForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

def signupOffer(request):
    if request.method == 'POST':
        form = SignUpOfferForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SignUpOfferForm()
    return render(request, 'registration/signupOffer.html', {'form': form})

def addNewOffer(request):
    form = AddNewOfferForm()
    return render(request,'offer/addNewOffer.html', {'form': form})


class OfertaViewset(viewsets.ModelViewSet):
    serializer_class = OfertaSerializer
    queryset = Oferta.objects.all()
