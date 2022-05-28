import boto3
from custom_encoder import buildResponse 

def handler(event, context):

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Users')

    result = table.scan()
    
    if 'Items' in result:
        body = {
            "mensaje": "Usuarios",
            "datos":result['Items']
        }
        
    else:
        body = {
            "mensaje": "Usuario no encontrado",
            "datos": result
        }

    response = buildResponse(200,body)

    return response