import boto3

def lambda_handler(event, context):
    # Entrada (json)
    nombre_bucket = event['body']['bucket']
    
    # Proceso
    s3 = boto3.client('s3')
    s3.create_bucket(Bucket=nombre_bucket, ACL='public-read')

    #Desactivación de bloqueo a ACL (instrucción pedida a IA)
    s3.put_public_access_block(
    Bucket=nombre_bucket,
    PublicAccessBlockConfiguration={
        'BlockPublicAcls': False,
        'IgnorePublicAcls': False,
        'BlockPublicPolicy': False,
        'RestrictPublicBuckets': False
    }
    )
    
    # Salida
    return {
        'statusCode': 200,
        'message': 'Bucket created successfully'
    }