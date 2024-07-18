import boto3

# Create an SNS client
sns_client = boto3.client('sns')

message = "Test message send using python SDK from AWS SNS test-topic"
topic_arn = 'arn:aws:sns:us-east-1:604476232840:test-topic'

response = sns_client.publish(
    Message=message,
    TopicArn=topic_arn
)

print(f"Message sent! Message ID: {response['MessageId']}")
