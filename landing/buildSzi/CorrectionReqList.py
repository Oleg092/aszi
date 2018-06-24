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
        newSziList = list()
        for szi in sziList:  # проходимся по всем СЗИ которые уже есть в системе, доставая списки покрываемых требований
            reqListInSzi = Defence.objects.values('requirements').filter(def_id=szi)
            for req in reqListInSzi:  # проходимся по всем требованиям и добавляем во мн-во id закрываемых требований
                reqClosedBySzi.add(req['requirements'])
        # таким образом получено мн-во, в котором указаны id всех закрываемых требований
        for req in reqList:
            if req['id'] not in reqClosedBySzi:  # если требование не закрыто, добавляем его в новый список
                newSziList.append(req['id'])
        print(reqClosedBySzi)
        print(newSziList)
        return newSziList

    def adaptationLevel2(self):
            if self.notUsingMobile:
                print(self.notUsingMobile)

            if self.notUsingVirtual:
                print('notUsingVirtual')

            if self.notUsingWireless:
                print('notUsingWireless')
            return 'hi'