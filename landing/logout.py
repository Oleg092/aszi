from django.views.generic import TemplateView
from landing.UserCookie import UserCookie


class LogOut(TemplateView):
    template_name = "landing/LogOut.html"

    # после нажатия кнопки logout обнуляются куки и пользователь редиректится на страницу авторизации
    def post(self, *args):
        context = UserCookie.delCookie()
        return context
