from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template import loader
from django import forms



site_hdr = "AppSec"

def index(request):
    return render(request, 'index.html', {'header': site_hdr})

def spellchecker(request):
    return render(request, 'spellchecker.html', {'header': site_hdr})

def imageresizer(request):
    return render(request, 'imageresizer.html', {'header': site_hdr})

