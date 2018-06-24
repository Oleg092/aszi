from abc import ABCMeta, abstractmethod, abstractproperty

from landing.models import Requirements


class BuildSziList():
    __metaclass__ = ABCMeta

    @abstractmethod
    def buildListSzi(self):
        """Подобрать СрЗИ"""

    @abstractmethod
    def exeptReq(self):
        """Список требований закрываемый существующими СрЗИ в системе"""

    @staticmethod
    @abstractmethod
    def adaptationLevel1(reqList, sziList):
        """Адаптация мер с учетом имеющихся в системе СЗИ"""

    @abstractmethod
    def adaptationLevel2(self, notUsingVirtual, notUsingWireless, notUsingMobile, reqList):
        """Тоже адаптация, не знаю как обозвать"""

    @staticmethod
    def getReqList(pdnLvl):
        """достаем список мер исходя из выбранного пользуном предполагаемого уровня защищенности"""
        """Тупой костыль, но гуглить времени нет"""
        range = [0, 1]
        if pdnLvl == 2:
            range = [0, 1, 2]
        if pdnLvl == 3:
            range = [0, 1, 2, 3]
        if pdnLvl == 4:
            range = [0, 1, 2, 3, 4]
        requirements = Requirements.objects.values('id').filter(pdn_lvl__in=range, defensible__gt=0)
        print(requirements)
        return requirements

