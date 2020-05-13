import json
import boto3
import decimal

dynamodb = boto3.resource('dynamodb')
eleccleanDB = dynamodb.Table('ElecClean')

def decimal_default(obj):
    if isinstance(obj, decimal.Decimal):
        return int(obj)
    raise TypeError

def handler(event, context):
    
    body = event["body"]
    print(body)
    request=json.loads(body)
    if not("PK" in request and "fraude" in request):
        return {
         'statusCode': 400,
         'body': "Bad Request"
        }
    
    response=eleccleanDB.update_item(
        Key={
            'PK': request["PK"]
        },
        UpdateExpression="set fraude = :f",
        ExpressionAttributeValues={
            ':f': request["fraude"]   
        },
        ReturnValues="ALL_NEW"
    )

    return {
     'statusCode': 200,
     'body': json.dumps(response["Attributes"],default=decimal_default)
    }
    
