import boto3
import json

client = boto3.client('comprehend')

message = 'The price was not bad, but the quality is not the grateates; and the delivery took 10 days.'

language_code = client.detect_dominant_language(Text=message)['Languages'][0]['LanguageCode']

response_key_phrase = client.detect_key_phrases(
    Text=message,
    LanguageCode=language_code
)
print(json.dumps(response_key_phrase, indent=4))

print("--------")