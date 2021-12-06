from time import sleep
from json import dumps
from kafka import KafkaProducer
import pandas as pd


producer = KafkaProducer(
        bootstrap_servers = ['localhost:9092'],
        value_serializer = lambda x:dumps(x).encode('utf-8')
        )

df_test = pd.read_csv('data/test_preprocessed.csv')
df_test = df_test.dropna()

for _, row in df_test.iterrows():
    data = {
        'X' : [row.tolist()]
        }
    producer.send('test', value=data)
    sleep(2)
