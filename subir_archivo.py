import boto3

def lambda_handler(event, context):
    # Entrada (json)
    nombre_bucket = event['body']['bucket']
    nombre_directorio = event['body']['directoryName']
    ruta = event['body']['filePath']
        
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

    s3.upload_file(Filename=ruta, Bucket=nombre_bucket, Key=full_key)
    
    # Salida
    return {
        'statusCode': 200,
        'message': 'File uploaded successfully'
    }