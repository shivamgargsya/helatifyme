from helathifyme.application.ingredients.models.ingredients import Ingredients,Ingredient
from helathifyme.application.units.models.units import Units,Unit
from helathifyme.application.unit_conversion.models.unit_conversion import UnitConversions,UnitConversion
class Driver():
    def __init__(self):
        pass

    def setup(self):
        Units.add(Unit('gm',1))
        Units.add(Unit('kg'),1)
        Units.add(Unit('unit'))
        Ingredients.add(Ingredient('rice',100,100,100,100))
        Ingredients.add(Ingredient('tomato',100,0,100,5))
        UnitConversions.add(UnitConversion(2,1,10))
