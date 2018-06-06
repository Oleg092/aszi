from django.conf.urls import url
from landing.home import HomePage
from landing.views import Autorization
from landing.logout import LogOut
from landing import getUserData

urlpatterns = [
    url(r'^landing/', Autorization.as_view()),
    url(r'^home/', HomePage.as_view()),
    url(r'^logout/', LogOut.as_view()),
    url(r'^xhr_test/', getUserData.xhr_test),#вызов функции обрабатывающей ajax
]
