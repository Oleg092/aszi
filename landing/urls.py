from django.contrib import admin
from django.conf.urls import url, include
from django.views.generic import TemplateView

from landing import views
from landing.views import Autarization


urlpatterns = [
    url(r'^landing/', Autarization.as_view()),

]