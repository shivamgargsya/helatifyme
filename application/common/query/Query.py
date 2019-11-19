from abc import ABC, abstractmethod
class Query(ABC):
    counter=0
    type = None


    def __init__(self):
        pass

    def add(self,value):
         # if type(value) != self.type:
         #    raise Exception('The object has to be of type %s' % str(self.type))
         value.id=self.counter+1
         self.counter+=1
         self.db.append(value)

    def get(self,id):
        items=list(filter[lambda item:item.id==id,self.db])
        if not items:
            return None
        return items[0]