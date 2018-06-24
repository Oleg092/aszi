from django.http import HttpResponse
from django.views.generic import TemplateView
import json

from landing.buildSzi.BuildSziList import BuildSziList
from landing.buildSzi.CorrectionReqList import CorrectionReqList


class BuildSziPage(TemplateView):  # """говнокласс с говнокодом для вызова остальных говноклассов"""
    template_name = 'landing/resultBuild.html'

    def post(self, request):
        if request.is_ajax():
            notUsingVirtual = request.POST["notUsingVirtual"]
            notUsingWireless = request.POST["notUsingWireless"]
            notUsingMobile = request.POST["notUsingMobile"]
            pdnLvl = request.POST["pdnLevel"]
            print(request.POST)
            reqList = BuildSziList.getReqList(int(pdnLvl))
            try:
                reqList = CorrectionReqList.adaptationLevel1(self, reqList, request.POST.getlist("listSzi[]"))
            except:
                print('none szi in system')
            #print(notUsingVirtual)
            #print(notUsingWireless)
            #print(notUsingMobile)
            #print(reqList)
            reqList2lvl = CorrectionReqList(bool(notUsingVirtual), bool(notUsingWireless), bool(notUsingMobile), reqList)
            reqList2lvl.adaptationLevel2()
            print(reqList2lvl.reqList)
        return HttpResponse('suka')