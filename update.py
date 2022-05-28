from decimal import Decimal
from custom_encoder import buildResponse
import json
import boto3
import logging
logger=logging.getLogger()
logger.setLevel(logging.INFO)


def handler(event, context):
    """Recibe un userid y un json con los datos a actualizar
    Args:
        userid (int): Identificador del usuario
        json (json): Datos a actualizar
        {
        "username":"Ronny Tobillos", (string)
        "age":5 (int)
        }
    Returns:
        http: 200 si el usuario existe y se actualizaron los datos
    """
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Users')
    userId = event.get('pathParameters').get('userid')
    body = json.loads(event.get('body'))
    username = body.get('username')
    age = body.get('age')
    
    try:
        #Si existe el usuario, procede a actualizarlo
        antes = table.get_item( TableName="Users", Key = { "userid": Decimal(userId) } )
        if 'Item' in antes:
            result = table.update_item(
                Key={
                    'userid': Decimal(userId)
                },
            ExpressionAttributeNames={
                '#todo_username': 'username',
                '#todo_age': 'age'
                },
            ExpressionAttributeValues={
                ':username': username,
                ':age': age
                },
                UpdateExpression='SET #todo_username = :username, #todo_age = :age',
                ReturnValues='UPDATED_NEW'
                )
            despues = table.get_item( TableName="Users", Key = { "userid": Decimal(userId) } )
            body = {
                "Message": "Usuario actualizado",
                "ANTES": antes,
                "DESPUES": despues,
                "result": result
            }
            response = buildResponse(200,body)
        else:
            #Si no existe el usuario, devuelve el mensaje de error
            body = {
                "Message": "Usuario no encontrado",
                "userid": userId
            }
            response = buildResponse(404,body)

        return response

    except:
        #Si no se puede consultar la tabla, se devuelve un error
        logger.exception(f'Error al tratar de consultar la base de datos !! {userId}')
        return buildResponse(500,{'Message':'Error al tratar de actualizar el usuario'})
    

    