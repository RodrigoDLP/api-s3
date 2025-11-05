import boto3

import base64
import boto3

def upload_base_64_to_s3(s3_bucket_name, s3_file_name, base_64_str):
    s3 = boto3.resource('s3')
    s3.Object(s3_bucket_name, s3_file_name).put(Body=base64.b64decode(base_64_str))
    return (s3_bucket_name, s3_file_name)

def lambda_handler(event, context);
    nombre_bucket = event['body']['bucket']
    filePath = event['body']['filePath']
    fileContent = event['body']['fileContent']
    upload_base_64_to_s3(nombre_bucket, filePath, fileContent)
    return {
        'statusCode': 200,
        'message': 'File uploaded successfully'
    }


"""
def lambda_handler(event, context):
    # Entrada (json)
    nombre_bucket = event['body']['bucket']
    nombre_directorio = event['body']['directoryName']
    ruta = event['body']['filePath']
    contenido = event['body']['fileContent']
        
    # Proceso
    s3 = boto3.client('s3')
    key_directorio = nombre_directorio
    if key_directorio[-1] != "/": 
        key_directorio += "/"
    nombre_archivo = ""
    for c in reversed(ruta):
        if c == "/":
            break
        nombre_archivo = c + nombre_archivo        
    full_key = key_directorio + nombre_archivo

    s3.upload_file(Filename=ruta, Bucket=nombre_bucket, Key=full_key, 
        ExtraArgs={'ACL': 'public-read'})
    
    # Salida
    return {
        'statusCode': 200,
        'message': 'File uploaded successfully'
    }"""