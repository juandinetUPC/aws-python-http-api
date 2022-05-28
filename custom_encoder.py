import json
from decimal import Decimal
class CustomEncoder(json.JSONEncoder):
    """Debido a que el json.dumps() no soporta el tipo Decimal, se crea una clase para convertir los tipos Decimal a int"""
    def default(self,obj):
        if isinstance(obj,Decimal):
            return int(obj)
        return json.JSONEncoder.default(self,obj)
    
def buildResponse(statusCode,body=None):
    """Recibe un código de estado y un diccionario con los datos a enviar en la respuesta"""
    response={
        'statusCode':statusCode,
        'headers':{
            'Content-Type':'application/json',
            'Access-Control-Allow-Origin':'*'
       }
   }
    if body is not None:
        #Si no se recibe un body, se devuelve un None
        response['body']=json.dumps(body,cls=CustomEncoder)
    return response