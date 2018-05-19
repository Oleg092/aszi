from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, FormView
from django.contrib import messages
from landing.models import Users
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
                # self.requestclient(request)
                return context
        except:
            print("not autorization")
            return self.form_valid(request)

    def form_valid(self, form):
        print('vizov')
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form1 = UsersForm(form.POST)
        if form1.is_valid():
            try:
                get_object_or_404(Users, email=form.POST["email"])
            except:
                form1.save()
                messages.success(form, "reg_success")
                context = HttpResponseRedirect('/landing')
                return context

        return self.requestclient(form)
        # return super().form_valid(form)

    def requestclient(self, request):
        print("wezdes")
        messages.success(request, "reg_failed")
        context = HttpResponseRedirect('/landing')
        context["data"] = 'auth_failed'
        return context
