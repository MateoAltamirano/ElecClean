import json
import boto3
from boto3.dynamodb.conditions import Key, Attr
from botocore.client import ClientError

dynamodb = boto3.resource('dynamodb')
appointments= dynamodb.Table('ElecClean')

def handler(event, context):
    try:
        # Scan
        items1 = appointments.scan()
        return {
            'statusCode': 200,
            'body': items1['Items']
        }
    except ClientError:
        return {
            'statusCode': 500,
            'body': 'Error in making database scan'
        }
    try:
        # Query
        data=event['queryStringParameters']['data']
        items2 = appointments.query(
            KeyConditionExpression=Key('doctor_id').eq(data)
        )
        return {
            'statusCode': 200,
            'body': items2['Items']
        }
    except ClientError:
        return {
            'statusCode': 500,
            'body': 'Error querying database'
        }