from django.http import HttpResponseRedirect


class UserCookie(object):  # класс для работы с cookie пользователя
    @staticmethod
    def setCookie(user):
        context = HttpResponseRedirect("/home")
        context.set_cookie("session", "true")
        context.set_cookie("user", user.id)
        context.set_cookie("userName", user.firstname)
        context.set_cookie("lastName", user.lastname)
        context.set_cookie("is_admin", user.is_admin)
        context.set_cookie("is_active", user.is_active)
        return context

    @staticmethod
    def delCookie():
        context = HttpResponseRedirect("/landing")
        context.set_cookie("session", "false")
        context.set_cookie("user", "none")
        context.set_cookie("userName", "none")
        context.set_cookie("lastName", "none")
        context.set_cookie("is_admin", "none")
        context.set_cookie("is_active", "none")
        return context
