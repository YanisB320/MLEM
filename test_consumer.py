from kafka import KafkaConsumer
from json import loads
import requests
import joblib as jl

consumer = KafkaConsumer(
    'test',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my_group',
     value_deserializer=lambda x: loads(x.decode('utf-8')))

model = jl.load('model/model.joblib')

for msg in consumer:
    prediction = model.predict(msg.value['X'])

    print('X: ' + str(msg.value['X']) + ' y: ' + str(prediction))
