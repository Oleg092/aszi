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
        while flag:
            i = 1
            firstResult = {a: 0 for a in range(count + 1)}
            while i <= count:
                reqListInSzi = Defence.objects.values("requirements").filter(def_id=i)
                for r in reqListInSzi:
                    if r["requirements"] in req:
                        firstResult[i] += 1
                i += 1
            maxReq = max(firstResult.items(), key=operator.itemgetter(1))[0]
            if maxReq == 0:
                break
            reqListInSzi = Defence.objects.values("requirements").filter(def_id=maxReq)
            result.append(maxReq)
            for r in reqListInSzi:
                if r['requirements'] in req:
                    req.remove(r['requirements'])
            if len(req) == 0:
                flag = False
            stop += 1
            if stop > count:
                flag = False
            firstResult.clear()

        print(req)
        print(result)
        print(datetime.datetime.now())
        return self