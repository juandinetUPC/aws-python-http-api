from decimal import Decimal
from custom_encoder import buildResponse
import boto3
import logging
logger=logging.getLogger()
logger.setLevel(logging.INFO)

def handler(event, context):
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Users')

    userId = event.get('pathParameters').get('userid')
    try:
        """ Dado un userid, intenta eliminarlo de la tabla
        Por ser el indice userid tipo 'N'(numero), se debe convertir el parametro(userId) a Decimal
        Para poder hacer la busqueda en la tabla"""
        
        # Se valída que el Usuario exista
        result = table.get_item( TableName="Users", Key = { "userid": Decimal(userId) } )
        if 'Item' in result:
            #Porcedemos a eliminar el usuario
            deleted = table.delete_item(Key={'userid': Decimal(userId)})
            body = {
            "operación": "delete_item",
            "Message": "success",
            'deleted': deleted,
            'userid': userId }
            response = buildResponse(200,body)
            
        else:
            #Si No existe el usuario retorna un 404
            body = {
                "Message": "Usuario no encontrado",
                "userid": userId
            }       
            response = buildResponse(404,body)
    

        return response
    except:
        logger.exception(f'Error al tratar de consultar la base de datos !! {userId}')
        return buildResponse(500,{'Message':'Error al tratar de eliminar el usuario'})
        