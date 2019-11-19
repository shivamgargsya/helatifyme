from flask import request
from flask_restplus import Resource
from helathifyme.v1_api import recepie_api as api
from schema import And, Optional, Schema, SchemaError
from helathifyme.application.common.utilities.utility import handle_exception,check_json
from helathifyme.application.ingredients.models.ingredients import Ingredients
from helathifyme.application.units.models.units import Units
from helathifyme.application.unit_conversion.models.unit_conversion import UnitConversions

base_path = '/recepie'

@api.route(base_path)
class RecepieResource(Resource):

    def validate_request(self,request_body):
        schema = Schema({'recepie': And(str),
                         }, ignore_extra_keys=True)
        try:
            schema.validate(request_body)
            for info in request_body['recepie'].splitlines():
                if len(info.split(','))!=3:
                    raise SchemaError('Each ingredient should have three fields separated by ,')
        except SchemaError as e:
            return e
        return True

    @handle_exception
    @check_json
    def post(self):
        request_body = request.get_json()
        is_valid = self.validate_request(request_body)
        if  not is_valid==True:
            return {is_valid.code},404
        ingredients_info=request_body['recepie'].splitlines( )
        ingredients=[]
        total_pfcf={"p_value":0.0,"c_value":0.0,"f_value":0.0,"fi_value":0.0}
        for info in ingredients_info:
            ingredient_detail=info.split(',').trim()
            ingredient=Ingredients.get_by_name(ingredient_detail[0])
            if not ingredient:
                continue
            quantity=float(ingredient_detail[1])
            unit = Units.get_by_name(ingredient_detail[2])
            if not unit:
                continue
            conversions=UnitConversions.get_by_unit_id_product_id(unit.id,ingredient.id)
            multiplication_factor=None
            if not conversions and not unit.multiplication_factor:
                continue
            if not conversions:
                multiplication_factor=unit.multiplication_factor
            else:
                multiplication_factor=conversions.mf
            multiplication_factor=float(multiplication_factor)/100.0
            p_value=multiplication_factor*quantity*ingredient.p_value
            c_value=multiplication_factor*quantity*ingredient.c_value
            fi_value=multiplication_factor*quantity*ingredient.fi_value
            f_value=multiplication_factor*quantity*ingredient.f_value
            total_pfcf['p_value']+=p_value
            total_pfcf['c_value']+=c_value
            total_pfcf['fi_value']+=fi_value
            total_pfcf['f_value']+=f_value
            ingredient_pfcf={"p_value":p_value,
                             "c_value":c_value,
                             "fi_value":fi_value,
                             "f_value":f_value,
                             "name":ingredient.name,
                             "unit":unit.name}
            ingredients.append(ingredient_pfcf)

        return {'total_pfcf':total_pfcf,"ingredients":ingredients},200


