import json
import boto3
from custom_encoder import buildResponse
from decimal import Decimal
import logging
logger=logging.getLogger()
logger.setLevel(logging.INFO)


def handler(event, context):

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Users')
    userId = event.get('pathParameters').get('userid')
    tipo=type(userId)
    
    try:
        """Por ser el indice userid tipo 'N'(numero), se debe convertir el parametro(userId) a Decimal
        Para poder hacer la busqueda en la tabla"""
        response = table.get_item( TableName="Users", Key = { "userid": Decimal(userId) } )

        if 'Item' in response:
            return buildResponse(200,response['Item'])
        else:
            return buildResponse(404,{'Message':'userid:%s not found' % userId})
    except:
        logger.exception(f'Error al tratar de consultar la base de datos !! {userId} tipo: {tipo}')
