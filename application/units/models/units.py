from helathifyme.application.common.query.Query import Query


class Unit():
    def __init__(self, name, multiplication_factor=None):
        self.id=None
        self.name = name
        self.multiplication_factor=multiplication_factor

    def stringify(self):
        {"name": self.name,
         "multiplication_factor": self.multiplication_factor,
         "id":self.id
         }


class Units(Query):
    db = [Unit]
    type = None
    __instance=None

    @staticmethod
    def getInstance():

        if Units.__instance == None:
            Units()
        return Units.__instance

    def __init__(self):
        if Units.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Units.__instance = self
        self.type = type(Unit)

    def get_by_name(self, name):
        units=list(filter(lambda item: item.name == name, self.db))
        if not units:
            return None
        return units[0]






