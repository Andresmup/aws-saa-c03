import boto3

sqs_client = boto3.client('sqs')

queue_url = 'https://sqs.us-east-1.amazonaws.com/604476232840/terraform-sqs.fifo'

response = sqs_client.receive_message(
    QueueUrl=queue_url,
    MaxNumberOfMessages=1,  
    WaitTimeSeconds=10,  
    VisibilityTimeout=30  
)

if 'Messages' in response:
    for message in response['Messages']:
        print(f"Message ID: {message['MessageId']}")
        print(f"Receipt Handle: {message['ReceiptHandle']}")
        print(f"Body: {message['Body']}")
        
        sqs_client.delete_message(
            QueueUrl=queue_url,
            ReceiptHandle=message['ReceiptHandle']
        )
        print('Mensaje eliminado')
else:
    print('No hay mensajes disponibles')