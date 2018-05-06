from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView

def landing(request):
    return render(request, 'landing/landing.html', locals())