import logging
import boto3
from botocore.exceptions import ClientError



def list_objects(bucket_name):
    try:
        s3_client = boto3.client('s3')
        contents = s3_client.list_objects_v2(Bucket=bucket_name)['Contents']

        for items in contents:
            print(items.get("Key"))
    except ClientError as e:
        logging.error(e)
        return False
    return True

list_objects("saa-c03-practice-bucket")