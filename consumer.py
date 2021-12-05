from kafka import KafkaConsumer
from json import loads
import requests

consumer = KafkaConsumer(
    'test',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my_group',
     value_deserializer=lambda x: loads(x.decode('utf-8')))

i = 0
for msg in consumer:
    if (i % 100 == 0):
        response = requests.get('http://localhost:8000/train')
        print(response.text)

    prediction = requests.post('http://localhost:8000/predict', json=msg.value)

    print(prediction.text)

    i += 1
