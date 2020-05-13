import json
import base64
import boto3
import io
import os
import json 
from PIL import Image
from requests_toolbelt.multipart import decoder


s3 = boto3.resource('s3')
dynamodb = boto3.resource('dynamodb')
eleccleanDB = dynamodb.Table('ElecClean')

def handler(event, context):
    
    bucket_images = os.environ['IMAGES_BUCKET']
    
    body = event["body"]

    content_type = event["headers"]["Content-Type"]

    body_dec = base64.b64decode(body)

    multipart_data = decoder.MultipartDecoder(body_dec, content_type)
    binary_content = []

    for part in multipart_data.parts:
        binary_content.append(part.content)
    
    imageStream = io.BytesIO(binary_content[0])
    imageFile = Image.open(imageStream)
    imageFile.save(imageStream,"JPEG")
    imageStream.seek(0)
    
    request = json.loads(binary_content[1])
    if not ("PK" in request and "colegio-ID" in request and "ciudad-ID" in request):
        return{
            'statusCode': 400,
            'body': "Bad Request"
        }
    
    s3.Bucket(bucket_images).put_object(ACL='public-read',Key=request["PK"]+'.jpeg', Body=imageStream)
    
    eleccleanDB.put_item(Item=request)
    
    return {
     'statusCode': 200,
     'body': json.dumps(request)
    }