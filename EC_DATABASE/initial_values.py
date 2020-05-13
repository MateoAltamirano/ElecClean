#!/usr/bin/python3
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ElecClean')

candidatos = ['Evo Morales','Carlos Mesa','Chi Hyun Chung']
ciudades = ['La Paz','Cochabamba','Santa Cruz','Oruro','Potosi','Tarija','Sucre','Pando','Beni']
colegios = ['San Ignacio','Calvert','Amor de Dios','Franco Boliviano','San Calixto','Don Bosco','La Salle','Montessori','Cumbre','Americano']

try:
    table.put_item(Item={'PK': 'total','candidato-1': 0,'candidato-2': 0,'candidato-3': 0})
    
    for i in range(1,4):
        pk = 'candidato-'+str(i)
        table.put_item(Item={'PK': pk,'info': candidatos[i-1]})
    for i in range(1,10):
        pk = 'ciu-'+str(i)
        table.put_item(Item={'PK': pk,'candidato-1': 0,'candidato-2': 0,'candidato-3': 0,'info':ciudades[i-1]})
  
    for i in range(1,11):
        pk = 'col-'+str(i)
        table.put_item(Item={'PK': pk,'candidato-1': 0,'candidato-2': 0,'candidato-3': 0,'info':colegios[i-1]})
        
    for i in range(1,5):
        pk = 'col-'+str(i)
        table.update_item(Key={'PK': pk}, UpdateExpression="SET #c = :c",
        ExpressionAttributeNames={'#c': 'ciudad-ID'},
        ExpressionAttributeValues={':c': 'ciu-1'},
        ReturnValues="UPDATED_NEW")
        
    for i in range(5,8):
        pk = 'col-'+str(i)
        table.update_item(Key={'PK': pk}, UpdateExpression="SET #c = :c",
        ExpressionAttributeNames={'#c': 'ciudad-ID'},
        ExpressionAttributeValues={':c': 'ciu-2'},
        ReturnValues="UPDATED_NEW")
    
    for i in range(8,11):
        pk = 'col-'+str(i)
        table.update_item(Key={'PK': pk}, UpdateExpression="SET #c = :c",
        ExpressionAttributeNames={'#c': 'ciudad-ID'},
        ExpressionAttributeValues={':c': 'ciu-3'},
        ReturnValues="UPDATED_NEW")   
        
    print('Filled table with initial values')
except Exception as e:
    print(e)