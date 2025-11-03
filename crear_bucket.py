import boto3

def lambda_handler(event, context):
    # Entrada (json)
    nombre_bucket = event['body']['bucket']

    # Proceso
    s3 = boto3.client('s3')
    s3.create_bucket(Bucket=nombre_bucket, ACL='public-read')
    
    # Salida
    return {
        'statusCode': 200,
        'message': 'Bucket created successfully'
    }