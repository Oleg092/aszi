from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, DetailView, ListView, FormView
from django.views.generic.base import RedirectView
from django.urls import reverse
import json
from django.contrib import messages

from landing.forms import UsersForm
from landing.models import Users


class Autorization(TemplateView, FormView):
    template_name = 'landing/landing.html'
    form_class = UsersForm

    def post(self, request):
        try:
            email = request.POST['email']
            pas = request.POST['pas']
            if email == "xxxx092@ya.ru" and pas == "123123":
                return HttpResponseRedirect('/landing')
            else:
                messages.success(request, "incorrect password or email")
                context = HttpResponseRedirect(request.path)
                return context
        except:
            self.form_valid(request)

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        return super().form_valid(form)
