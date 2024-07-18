import boto3
import json
# Create SQS client
sqs = boto3.client('sqs')

queue_url = 'https://sqs.us-east-1.amazonaws.com/604476232840/standard-test'

# Receive message from SQS queue
response = sqs.receive_message(
    QueueUrl=queue_url,
    AttributeNames=[
        'SentTimestamp'
    ],
    MaxNumberOfMessages=1,
    MessageAttributeNames=[
        'All'
    ],
    VisibilityTimeout=0,
    WaitTimeSeconds=0
)

print(json.dumps(response, indent = 2))

receipt_handle = response['Messages'][0]['ReceiptHandle']

message_id = response['Messages'][0]['MessageId']

sqs.delete_message(
    QueueUrl=queue_url,
    ReceiptHandle=receipt_handle
)

print('Received and deleted message: %s' % message_id)