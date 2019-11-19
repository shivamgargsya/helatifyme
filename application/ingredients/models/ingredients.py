from helathifyme.application.common.query.Query import Query
class Ingredient():
    def __init__(self,name,p_value,f_value,c_value,fi_value):
        self.id=None
        self.name=name
        self.p_value=p_value
        self.f_value=f_value
        self.fi_value=fi_value
        self.c_value=c_value

    def stringify(self):
        {"name":self.name,
         "p_value":self.p_value,
         "f_value":self.f_value,
         "fi_value":self.fi_value,
         "c_value":self.c_value
         }

class Ingredients(Query):
    db=[]
    type=None
    __instance=None

    @staticmethod
    def getInstance():

        if Ingredients.__instance == None:
            Ingredients()
        return Ingredients.__instance

    def __init__(self):
        if Ingredients.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Ingredients.__instance = self
        self.type=type(Ingredient)

    def get_by_name(self,name:str):
        ingredients=list(filter(lambda item:item.name==name,self.db))
        if ingredients:
            return ingredients[0]
        return None




