from django.conf.urls import url
from landing.home import HomePage
from landing.views import Autorization
from landing.logout import LogOut
from landing import getUserData, getManagementData

urlpatterns = [
    url(r'^landing/', Autorization.as_view()),
    url(r'^home/', HomePage.as_view()),
    url(r'^logout/', LogOut.as_view()),
    url(r'^xhr_test/', getUserData.xhr_test),
    url(r'^get_management_data/', getManagementData.getManagementData),
]
