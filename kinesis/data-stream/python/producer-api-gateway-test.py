import requests
import json
import base64
import random
from faker import Faker
fake = Faker()

for i in range(1,42):
    print("Numero de envio", i)

    # Datos que se incluirán en el campo "Data"
    inner_data = {
        "name": fake.unique.first_name(),
        "age": random.randint(18,70)
    }
    print("inner_data", inner_data)
    
    # Convertir el JSON a una cadena Base64
    json_inner_data = json.dumps(inner_data)
    base64_inner_data = base64.b64encode(json_inner_data.encode()).decode()

    # Cuerpo de la solicitud
    body = {
        "StreamName": "dev-kinesis",
        "Data": base64_inner_data,
        "PartitionKey": "test-partition-01"
    }

    print("body", body)
    # URL a la que se hace la solicitud POST
    url = "https://f6vrtfz1xh.execute-api.us-east-1.amazonaws.com/data-ingestion-001/data"

    # Encabezados de la solicitud
    headers = {
        "Content-Type": "application/json"
    }

    # Hacer la solicitud POST
    response = requests.post(url, headers=headers, data=json.dumps(body))

    # Imprimir la respuesta
    print(response.status_code)
    print(response.json())
    print("--------------------")