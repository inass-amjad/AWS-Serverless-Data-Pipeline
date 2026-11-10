import json
import urllib.parse
import boto3


s3 = boto3.client('s3')

def lambda_handler(event, context):
 
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
  
    file_name = key.split('/')[-1] 
    destination_key = f"processed/{file_name}"
    
    print(f"--- TRIGGERED! ---")
    print(f"Processing file: {key}")
    
    try:
       
        copy_source = {'Bucket': source_bucket, 'Key': key}
        s3.copy_object(Bucket=source_bucket, CopySource=copy_source, Key=destination_key)
        
        print(f"Success! File copied to {destination_key}")
        
    except Exception as e:
        print(f"Error: {e}")
        raise e
    
    return {
        'statusCode': 200,
        'body': json.dumps('Success! File moved to processed.')
    }
