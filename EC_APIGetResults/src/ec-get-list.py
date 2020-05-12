import json
import boto3
from boto3.dynamodb.conditions import Key, Attr
from botocore.client import ClientError
import decimal
 
def decimal_default(obj):
    if isinstance(obj, decimal.Decimal):
        return int(obj)
    raise TypeError

dynamodb = boto3.resource('dynamodb')
elecclean= dynamodb.Table('ElecClean')

def handler(event, context):
    data=event['queryStringParameters']['list']
    if data=="ciudad":
        try:
            items2 = elecclean.scan()
            arrayResp=[]
            for item in items2['Items']:
                if item['PK'][0:4]=="ciu-":
                    arrayResp.append(item)
            val =json.dumps(arrayResp, indent=2, default=decimal_default)
            val2 = json.loads(val)
            return {
                'statusCode': 200,
                'body': json.dumps(val2),
                "headers": {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'
                }
            }
        except ClientError:
            return {
                'statusCode': 500,
                'body': 'Error querying database',
                "headers": {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'
                }
            }
    elif data=="colegio":
        try:
            items2 = elecclean.scan()
            arrayResp=[]
            for item in items2['Items']:
                if item['PK'][0:4]=="col-":
                    arrayResp.append(item)
            val =json.dumps(arrayResp, indent=2, default=decimal_default)
            val2 = json.loads(val)
            return {
                'statusCode': 200,
                'body': json.dumps(val2),
                "headers": {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'
                }
            }
        except ClientError:
            return {
                'statusCode': 500,
                'body': 'Error querying database',
                "headers": {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'
                }
            }
    elif data=="candidato":
        try:
            items2 = elecclean.scan()
            arrayResp=[]
            for item in items2['Items']:
                if item['PK'][0:9]=="candidato":
                    arrayResp.append(item)
            val =json.dumps(arrayResp, indent=2, default=decimal_default)
            val2 = json.loads(val)
            return {
                'statusCode': 200,
                'body': json.dumps(val2),
                "headers": {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'
                }
            }
        except ClientError:
            return {
                'statusCode': 500,
                'body': 'Error querying database',
                "headers": {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'
                }
            }
    else:
        return {
            'statusCode': 500,
            'body': 'Invalid command',
            "headers": {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            }
        }
        
    
    