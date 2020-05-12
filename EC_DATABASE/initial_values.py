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
    print('Filled table with initial values')
except Exception as e:
    print(e)