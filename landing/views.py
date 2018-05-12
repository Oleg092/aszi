from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, DetailView, ListView
from django.views.generic.base import RedirectView
from django.urls import reverse
import json
from django.contrib import messages


class Autarization(TemplateView):
    template_name = 'landing/landing.html'

    def post(self, request):
        email = request.POST['email']
        pas = request.POST['pas']
        if email == "xxxx092@ya.ru" and pas == "123123":
            return HttpResponseRedirect('/landing')
        else:
            messages.success(request, "incorrect password or email")
            context = HttpResponseRedirect(request.path)
            return context



