from kafka import KafkaConsumer
from json import loads
import requests

consumer = KafkaConsumer(
    'train',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my_group',
     value_deserializer=lambda x: loads(x.decode('utf-8')))

for msg in consumer:
    response = requests.post('http://localhost:8000/train', json=msg.value)
