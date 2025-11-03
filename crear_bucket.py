import boto3

def lambda_handler(event, context):
    # Entrada (json)
    nombre_bucket = event['body']['bucket']
    
    # Proceso
    s3 = boto3.client('s3')
    s3.create_bucket(Bucket=nombre_bucket)

    #Desactivación de bloqueo a ACL y ownership controls 
    #(instrucciones pedidas a IA debido a errores)
    s3.put_bucket_ownership_controls(
        Bucket=nombre_bucket, OwnershipControls={'Rules': [{'ObjectOwnership': 'ObjectWriter'}]})

    s3.put_public_access_block(
    Bucket=nombre_bucket,
    PublicAccessBlockConfiguration={
        'BlockPublicAcls': False,
        'IgnorePublicAcls': False,
        'BlockPublicPolicy': False,
        'RestrictPublicBuckets': False
    })
    s3.put_bucket_acl(Bucket=nombre_bucket, ACL='public-read')

    
    # Salida
    return {
        'statusCode': 200,
        'message': 'Bucket created successfully'
    }