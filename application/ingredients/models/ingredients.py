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
    db=[Ingredient]
    __instance = None
    type=None
    def __init__(self):
        super(Ingredients,self).__init__()
        Ingredients.type=Ingredient

    def get_by_name(self,name):
        ingredients=list(filter(lambda item:item.name==name,self.db))
        if ingredients:
            return ingredients[0]
        return None




