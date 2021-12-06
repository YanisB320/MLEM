from time import sleep
from json import dumps
from kafka import KafkaProducer
import pandas as pd


producer = KafkaProducer(
        bootstrap_servers = ['localhost:9092'],
        value_serializer = lambda x:dumps(x).encode('utf-8')
        )

df_train = pd.read_csv('data/train_preprocessed.csv')
df_train = df_train.dropna()
# df_test = pd.read_csv('data/test_preprocessed.csv')
# df_test = df_test.dropna()

X = df_train.iloc[:,1:]
y = df_train.iloc[:,0]

i = 0
for _, row in X.iterrows():
    data_train = {
        'X' : [row.tolist()],
        'y' : int(y.iloc[i])
        }
    # data_test = {
    #     'X' : [row.tolist()]
    #     }
    producer.send('train', value=data_train)
    # producer.send('train', value=data_test)

    i += 1

    sleep(5)
