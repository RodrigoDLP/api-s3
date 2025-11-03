import boto3

def lambda_handler(event, context):
    # Entrada (json)
    nombre_bucket = event['body']['bucket']
    nombre_directorio = event['body']['directoryName']
    key_directorio = nombre_directorio
    if key_directorio[-1] != "/":
        key_directorio += "/"
    
    # Proceso
    s3 = boto3.client('s3')
    s3.put_object(Bucket=nombre_bucket, Key=key_directorio, ACL='public-read')
    
    # Salida
    return {
        'statusCode': 200,
        'message': 'Directory created successfully'
    }