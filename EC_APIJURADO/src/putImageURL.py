import json
import boto3
import decimal
import os

dynamodb = boto3.resource('dynamodb')
eleccleanDB = dynamodb.Table('ElecClean')

def decimal_default(obj):
    if isinstance(obj, decimal.Decimal):
        return int(obj)
    raise TypeError

def handler(event, context):
    
    request = event['Records'][0]
    
    res = 'https://'
    res += request['s3']['bucket']['name']
    res += '.S3.'
    res += request['awsRegion']
    res += '.amazonaws.com/'
    
    key = request['s3']['object']['key']
    
    res += key
    
    
    response=eleccleanDB.update_item(
        Key={
            'PK': key.split('.')[0]
        },
        UpdateExpression="set #fn = :u",
        ExpressionAttributeValues={
            ':u': res  
        },
        ExpressionAttributeNames= {
            "#fn":"foto-url"
        },     
        ReturnValues="ALL_NEW"
    )
    

    return {
     'statusCode': 200,
     'body': json.dumps(response["Attributes"],default=decimal_default)
    }
    
