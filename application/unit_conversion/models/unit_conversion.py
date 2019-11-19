from helathifyme.application.common.query.Query import Query

class UnitConversion():
    def __init__(self, unit_id, ingredient_id,mf):
        self.id=None
        self.unit_id = unit_id
        self.ingredient_id = ingredient_id
        self.mf=mf

    def stringify(self):
        {
         "id":self.id,
         "unit_id": self.unit_id,
         "mf": self.mf,
         "ingredient_id":self.ingredient_id
         }


class UnitConversions(Query):
    db = []
    type = None
    __instance=None

    @staticmethod
    def getInstance():

        if UnitConversions.__instance == None:
            UnitConversions()
        return UnitConversions.__instance

    def __init__(self):
        if UnitConversions.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            UnitConversions.__instance = self
        self.type = type(UnitConversion)

    def get_by_unit_id_product_id(self, unit_id,product_id):
        conversion=list(filter(lambda item: item.unit_id == unit_id and item.product_id==product_id, self.db))
        if conversion:
            return conversion[0]
        return None









