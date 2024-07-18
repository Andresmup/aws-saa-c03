import boto3
import json

client = boto3.client('comprehend')

message = 'The price was not bad, but the quality is not the grateates; and the delivery took 10 days.'

response = client.detect_dominant_language(Text=message)

print(json.dumps(response, indent=4))

print("--------")

print(response['Languages'][0]['LanguageCode'])