from django.http import HttpResponse
from django.views.generic import TemplateView
import json
import datetime

from landing.buildSzi.BuildSziList import BuildSziList
from landing.buildSzi.CorrectionReqList import CorrectionReqList
from landing.buildSzi.StandartAlg import CreateStandartSziList


class BuildSziPage(TemplateView):  # """говнокласс с говнокодом для вызова остальных говноклассов"""
    template_name = 'landing/resultBuild.html'

    def post(self, request):
        if request.is_ajax():
            print(datetime.datetime.now())
            notUsingVirtual = request.POST["notUsingVirtual"]
            notUsingWireless = request.POST["notUsingWireless"]
            notUsingMobile = request.POST["notUsingMobile"]
            pdnLvl = request.POST["pdnLevel"]
            print(request.POST)
            reqList = BuildSziList.getReqList(int(pdnLvl))
            fullReqList = request.POST.getlist("listSzi[]")
            try:
                if request.POST["listSzi[]"] != None:
                    reqList = CorrectionReqList.adaptationLevel1(self, reqList, fullReqList)
            except:
                print('none szi in system')
            reqList2lvl = CorrectionReqList(bool(notUsingVirtual), bool(notUsingWireless), bool(notUsingMobile), reqList)
            reqList2lvl.adaptationLevel2()
            sziList = CreateStandartSziList(reqList2lvl.reqList)
            sziList.buildListSzi()
        return HttpResponse('suka')