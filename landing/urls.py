from django.conf.urls import url
from landing.home import HomePage
from landing.views import Autorization



urlpatterns = [
    url(r'^landing/', Autorization.as_view()),
    url(r'^home/', HomePage.as_view())
]