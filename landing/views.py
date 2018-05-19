from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext
from django.views.generic import TemplateView, FormView
import json
from django.contrib import messages

from landing.forms import UsersForm


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
                context["data"] = 'auth_failed'
                #self.requestclient(request)
                return context
        except:
            print("not autorization")
        return self.requestclient(request)

    def form_valid(self, form):
        print('vizov')
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        self.requestclient(form)
        ###form.save()
        #return super().form_valid(form)

    def requestclient(self, request):
        print("wezdes")
        messages.success(request, "reg")
        context = HttpResponseRedirect('/landing')
        context["data"] = 'auth_failed'
        return context
