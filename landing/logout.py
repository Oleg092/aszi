from django.views.generic import TemplateView
from django.http import HttpResponseRedirect


class LogOut(TemplateView):
    template_name = "landing/LogOut.html"

    #после нажатия кнопки logout обнуляются куки и пользователь редиректится на страницу авторизации
    def post(self, *args):
        context = HttpResponseRedirect("/landing")
        context.set_cookie("session", "false")
        context.set_cookie("user", "none")
        context.set_cookie("userName", "none")
        context.set_cookie("lastName", "none")
        context.set_cookie("is_admin", "none")
        context.set_cookie("is_active", "none")
        return context