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
    try:
        # Query
        data=event['queryStringParameters']['pk']
        items2 = elecclean.query(
            KeyConditionExpression=Key('PK').eq(data)
        )
        val =json.dumps(items2['Items'], indent=2, default=decimal_default)
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