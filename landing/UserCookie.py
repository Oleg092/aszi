from django.http import HttpResponseRedirect


class UserCookie(object):
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
