from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, FormView
from django.contrib import messages
from landing.models import Users
from landing.forms import UsersForm
from landing.UserCookie import UserCookie
import hashlib


class Autorization(TemplateView, FormView):
    template_name = 'landing/landing.html'
    form_class = UsersForm

    def post(self, request):
        try:
            email = request.POST['email']
            pas = request.POST['pas']
            pas = bytes(pas, encoding='UTF-8')
            pas = hashlib.md5(pas).hexdigest()
            try:
                user = get_object_or_404(Users, email=email)
            except:
                messages.success(request, "user not found")
                self.requestclient(request)
            if user.password == pas:
                context = UserCookie.setCookie(user)
                return context
            else:
                messages.success(request, "incorrect password or email")
                context = HttpResponseRedirect(request.path)
                context["data"] = 'auth_failed'
                return context
        except:
            print("not autorization")
            return self.form_valid(request)

    def form_valid(self, form):
        form1 = UsersForm(form.POST)
        if form1.is_valid():
            try:
                get_object_or_404(Users, email=form.POST["email"])
            except:
                form1.save()
                messages.success(form, "reg_success")
                context = HttpResponseRedirect('/landing')
                return context

        messages.success(form, "reg_failed")
        return self.requestclient(form)

    def requestclient(self, request):
        context = HttpResponse('failed')
        return context

