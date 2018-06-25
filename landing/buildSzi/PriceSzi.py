from landing.buildSzi.BuildSziList import BuildSziList


class PriceSzi(BuildSziList):
    def __init__(self, sziList):
        self.sziList = sziList

    def getListPrice(self):
        """делаем тут ассоциативный массив из срзи, методов обслуживания и стоимости этих методов, а пока заглушка"""
