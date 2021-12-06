from kafka import KafkaConsumer
from json import loads
import requests
import os.path
import joblib as jl
from sklearn import linear_model

consumer = KafkaConsumer(
    'train',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my_group',
     value_deserializer=lambda x: loads(x.decode('utf-8')))


model = None

if (os.path.isfile('model/model.joblib')):
    model = jl.load('model/model.joblib')
else:
    model = linear_model.SGDClassifier()

for msg in consumer:
    model.partial_fit(msg.value['X'], [msg.value['y']], classes=[0, 1])
    print("train model on " + str(msg.value['X']))

    # save model
    jl.dump(model, 'model/model.joblib')
