import boto3
import json

client = boto3.client('comprehend')

message = 'Ey dome ass, sfo, piece of crab, u nigga, macac, uuh uh'

language_code = client.detect_dominant_language(Text=message)['Languages'][0]['LanguageCode']

response_toxic_content = client.detect_toxic_content(
    TextSegments=[
        {
            'Text': message
        },
    ],
    LanguageCode=language_code
)

print(json.dumps(response_toxic_content, indent=4))
