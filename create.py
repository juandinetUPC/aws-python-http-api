import json
import boto3
from decimal import Decimal
from custom_encoder import buildResponse
import logging
logger=logging.getLogger()
logger.setLevel(logging.INFO)

def handler(event, context):
   
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Users')
    item = json.loads(event.get('body'))
    userId=item.get('userid')
       
    try:
        ifExist = table.get_item( TableName="Users", Key = { "userid": Decimal(userId) } )
        
        if 'Item' in ifExist:
            #Si existe el usuario, envía el mensaje de error
            body={'Message':'Usuario ya existe',
                  "User":ifExist['Item']}
            return buildResponse(202,body)
        
        else:
            #Si no existe el usuario, lo inserta en la tabla    
            table.put_item(Item=item)

            body = {
                "mensaje": "Usuario creado",
                "User": item
            }
            response = buildResponse(201,body)
            return response
    except:
        logger.exception(f'Error al tratar de conectarse a la base de datos !! {userId}')
        return buildResponse(500,{'Message':'Error al tratar de crear el usuario'})