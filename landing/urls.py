from django.conf.urls import url
from landing.home import HomePage
from landing.views import Autorization
from landing.logout import LogOut
from landing import getUserData, getReqList, getSziList
from landing.buildSzi.buildSziController import BuildSziPage

urlpatterns = [
    url(r'^landing/', Autorization.as_view()),
    url(r'^home/', HomePage.as_view()),
    url(r'^logout/', LogOut.as_view()),
    url(r'^getUserList/', getUserData.getUsersList),
    url(r'^get_req_list/', getReqList.getReqList),
    url(r'^getSziList/', getSziList.getSziList),
    url(r'^build_szi_list/', BuildSziPage.as_view()),
]
