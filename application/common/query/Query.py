from abc import ABC, abstractmethod
class Query(ABC):
    db = []
    counter=0
    __instance = None
    type = None

    @staticmethod
    def getInstance():

        if Query.__instance == None:
            Query()
        return Query.__instance

    def __init__(self):

        if Query.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Query.__instance = self

    def add(self,value):
         if type(value) != self.type:
            raise Exception('The object has to be of type %s' % str(self.type))
         value.id=self.counter+1
         self.counter+=1
         self.db.append(value)

    def get(self,id):
        items=list(filter[lambda item:item.id==id,self.db])
        if not items:
            return None
        return items[0]