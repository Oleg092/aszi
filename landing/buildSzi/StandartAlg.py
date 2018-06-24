from landing.buildSzi.BuildSziList import BuildSziList
from landing.models import Defence
import operator
import datetime


class CreateStandartSziList(BuildSziList):
    def __init__(self, reqList):
        self.reqList = reqList
        self.sziList = None

    def buildListSzi(self):
        req = set()
        flag = True
        count = Defence.objects.count()
        stop = 1
        maxReq = 0
        result = list()
        for r in self.reqList:  # получаем мн-во мер, которые необходимо закрыть
            req.add(r)
        while flag:  # подбор идет пока флаг = true
            i = 1
            firstResult = {a: 0 for a in range(count + 1)}  # этот словарь заполняется id szi и кол-вом мер, которые
            # они закрывают
            while i <= count:  # проходимся по всем срзи
                reqListInSzi = Defence.objects.values("requirements").filter(def_id=i)
                for r in reqListInSzi:
                    if r["requirements"] in req:  # выясняем сколько мер закрывает выбранная сзи
                        firstResult[i] += 1
                i += 1
            maxReq = max(firstResult.items(), key=operator.itemgetter(1))[0]  # получаем номер срзи, с max числ закр мер
            if maxReq == 0:
                break
            reqListInSzi = Defence.objects.values("requirements").filter(def_id=maxReq)  # достаем срзи с max закр мер
            result.append(maxReq)
            for r in reqListInSzi:
                if r['requirements'] in req:
                    req.remove(r['requirements'])  # исключаем из требований те меры, которые закрывает выбранная срзи
            if len(req) == 0:  # если не осталось мер, которые надо закрыть, завершаем цикл
                flag = False
            stop += 1
            if stop > count:  # если не удается закрыть все требования, останавливаем цикл
                flag = False
            firstResult.clear()

        print(req)
        print(result)
        print(datetime.datetime.now())  # проверка времени, за которое отрабатывает алгоритм... для 50 срзи в базе
        # поиск на моем слабеньком компе происходит за 0.12 сек на 1 уровне ПДН и за 0.24 сек на 4 уровне ПДН
        return self
