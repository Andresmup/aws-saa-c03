import boto3

sqs_client = boto3.client('sqs')

queue_url = 'https://sqs.us-east-1.amazonaws.com/604476232840/terraform-sqs.fifo'

response = sqs_client.send_message(
    QueueUrl=queue_url,
    MessageBody='This is a message send throw SNS',
    MessageGroupId='group1',
    MessageDeduplicationId='deduplication-id-2'
)

print(f"Message sent! Message ID: {response['MessageId']}")

