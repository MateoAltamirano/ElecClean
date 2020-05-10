import os
import boto3
from boto3.dynamodb.conditions import Key
import decimal
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ElecClean')

def handler(event, context):
    pk = event['Records'][0]['dynamodb']['Keys']['PK']['S']
    eventName = event['Records'][0]['eventName']

    if 'm-' in pk and eventName != 'REMOVE':
        record = event['Records'][0]['dynamodb']
        colegio_ID = record['NewImage']['colegio-ID']['S']
        ciudad_ID = record['NewImage']['ciudad-ID']['S']
 
        candidato_1 = int(record['NewImage']['candidato-1']['N'])
        candidato_2 = int(record['NewImage']['candidato-2']['N'])
        candidato_3 = int(record['NewImage']['candidato-3']['N'])
        
        colegio = json.loads(json.dumps(table.get_item(Key={'PK': colegio_ID}), default=decimal_default))
        ciudad = json.loads(json.dumps(table.get_item(Key={'PK': ciudad_ID}), default=decimal_default))
        total = json.loads(json.dumps(table.get_item(Key={'PK': 'total'}), default=decimal_default))
        
        if eventName == 'INSERT':
            col_c1 = colegio['Item']['candidato-1']+candidato_1
            col_c2 = colegio['Item']['candidato-2']+candidato_2
            col_c3 = colegio['Item']['candidato-3']+candidato_3
            
            ciu_c1 = ciudad['Item']['candidato-1']+candidato_1
            ciu_c2 = ciudad['Item']['candidato-2']+candidato_2
            ciu_c3 = ciudad['Item']['candidato-3']+candidato_3
            
            total_c1 = total['Item']['candidato-1']+candidato_1 if 'Item' in total else candidato_1
            total_c2 = total['Item']['candidato-2']+candidato_2 if 'Item' in total else candidato_2
            total_c3 = total['Item']['candidato-3']+candidato_3 if 'Item' in total else candidato_3
            print(total_c1,total_c2,total_c3)
            try:
                updateTable(colegio_ID,ciudad_ID,col_c1,col_c2,col_c3,ciu_c1,ciu_c2,ciu_c3,total_c1,total_c2,total_c3,total)
            except Exception as e:
                print(e)
        elif eventName == 'MODIFY':
            print('MODIFIED')

    return "UPDATE CHECK TABLE"


def updateTable(colegio_ID,ciudad_ID,col_c1,col_c2,col_c3,ciu_c1,ciu_c2,ciu_c3,total_c1,total_c2,total_c3,total):
    table.update_item(Key={'PK': colegio_ID}, UpdateExpression="SET #c1 = :c1, #c2 = :c2, #c3 = :c3",
    ExpressionAttributeNames={'#c1': 'candidato-1',
                              '#c2': 'candidato-2',
                              '#c3': 'candidato-3'},
    ExpressionAttributeValues={
        ':c1': col_c1,
        ':c2': col_c2,
        ':c3': col_c3,
    },
    ReturnValues="UPDATED_NEW")
    
    table.update_item(Key={'PK': ciudad_ID}, UpdateExpression="SET #c1 = :c1, #c2 = :c2, #c3 = :c3",
    ExpressionAttributeNames={'#c1': 'candidato-1',
                              '#c2': 'candidato-2',
                              '#c3': 'candidato-3'},
    ExpressionAttributeValues={
        ':c1': ciu_c1,
        ':c2': ciu_c2,
        ':c3': ciu_c3,
    },
    ReturnValues="UPDATED_NEW")
    
    if 'Item' in total:
        table.update_item(Key={'PK': 'total'}, UpdateExpression="SET #c1 = :c1, #c2 = :c2, #c3 = :c3",
        ExpressionAttributeNames={'#c1': 'candidato-1',
                                  '#c2': 'candidato-2',
                                  '#c3': 'candidato-3'},
        ExpressionAttributeValues={
            ':c1': total_c1,
            ':c2': total_c2,
            ':c3': total_c3,
        },
        ReturnValues="UPDATED_NEW")
    else:
        table.put_item(Item={'PK': 'total','candidato-1': total_c1,'candidato-2': total_c2,'candidato-3': total_c3})

def decimal_default(obj):
    if isinstance(obj, decimal.Decimal):
        return int(obj)
    raise TypeError