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

for msg in consumer:
    prediction = requests.post('http://localhost:8000/predict', json=msg.value)

    print(prediction.text)

