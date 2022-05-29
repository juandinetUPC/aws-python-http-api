import boto3
from custom_encoder import buildResponse 

def handler(event, context):
    """Devuelve una lista de usuarios"""
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Users')
    #Obtiene todos los usuarios
    result = table.scan()
    
    if 'Items' in result:
        #Si hay usuarios, devuelve la lista
        body = {
            "Message": "Usuarios",
            "datos":result['Items']
        }
        response = buildResponse(200,body)
        
    else:
        #Si no hay usuarios, devuelve el mensaje de error
        body = {
            "Message": "La tabla está vacía",
            "datos": result
        }
        response = buildResponse(204,body)

    return response