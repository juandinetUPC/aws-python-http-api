import json
import boto3


def handler(event, context):
   
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Users')
   
    item = json.loads(event.get('body'))
    #test
    #item = event
   
    table.put_item(Item=item)

    body = {
        "mensaje": "Usuario creado",
        "datos": item
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
