import boto3

# Create SQS client
sqs = boto3.client('sqs')

queue_url = 'https://sqs.us-east-1.amazonaws.com/604476232840/standard-test'

# Send message to SQS queue
response = sqs.send_message(
    QueueUrl=queue_url,
    DelaySeconds=10,
    MessageAttributes={
        "Title": {
            "DataType": "String",
            "StringValue": "Titaninc"
        },
        "Gender": {
            "DataType": "String",
            "StringValue": "Love"
        },
        "Year": {
            "DataType": "Number",
            "StringValue": "1998"
        }
    },
    MessageBody=(
        'Information about the last film added.'
    )
)

print(response['MessageId'])