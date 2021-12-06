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

if (os.path.isfile('model.joblib')):
    model = jl.load('model.joblib')

for msg in consumer:
    if msg.value.get("y", None) is not None: # train if we have a label

        if not model:
            model = linear_model.SGDClassifier()

        model.partial_fit(msg.value['X'], [msg.value['y']], classes=[0, 1])
        print("train model on " + str(msg.value['X']))

        # save model
        jl.dump(model, 'model.joblib')
    else: # else test
        if model is not None:
            prediction = model.predict(msg.value['X'])
            print('predict y: ' + str(prediction) + ' with X: ' + str(msg.value['X']))
