from helathifyme.application.common.query.Query import Query


class Unit():
    def __init__(self, name, multiplication_factor):
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
    __instance = None
    type = None

    def __init__(self):
        super(Units, self).__init__()
        Units.type = Unit

    def get_by_name(self, name):
        units=list(filter(lambda item: item.name == name, self.db))
        if not units:
            return None
        return units[0]






