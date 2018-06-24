from landing.buildSzi.BuildSziList import BuildSziList
from landing.models import Defence


class CorrectionReqList(BuildSziList):

    def __init__(self, notUsingVirtual, notUsingWireless, notUsingMobile, reqList):
        self.notUsingVirtual = notUsingVirtual
        self.notUsingWireless = notUsingWireless
        self.notUsingMobile = notUsingMobile
        self.reqList = reqList

    def adaptationLevel1(self, reqList, sziList):
        reqClosedBySzi = set()
        newReqList = list()
        for szi in sziList:  # проходимся по всем СЗИ которые уже есть в системе, доставая списки покрываемых требований
            reqListInSzi = Defence.objects.values('requirements').filter(def_id=szi)
            for req in reqListInSzi:  # проходимся по всем требованиям и добавляем во мн-во id закрываемых требований
                reqClosedBySzi.add(req['requirements'])
        # таким образом получено мн-во, в котором указаны id всех закрываемых требований
        for req in reqList:
            if req not in reqClosedBySzi:  # если требование не закрыто, добавляем его в новый список
                newReqList.append(req)
        return newReqList

    def adaptationLevel2(self):
        wireless = [20, 109]
        virtual = [74, 73, 72, 71, 70, 69, 68, 67, 66, 65]
        if self.notUsingMobile:
            if 21 in self.reqList:
                self.reqList.remove(21)

        if self.notUsingVirtual:
            for v in virtual:
                if v in self.reqList:
                    self.reqList.remove(v)

        if self.notUsingWireless:
            for w in wireless:
                if w in self.reqList:
                    self.reqList.remove(w)
        return self
