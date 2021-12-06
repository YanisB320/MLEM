#!/bin/bash

virtualenv venv
source ./venv/bin/activate
pip install -r requirements.txt

# install kafka
wget https://dlcdn.apache.org/kafka/3.0.0/kafka_2.13-3.0.0.tgz
tar -xzf kafka_2.13-3.0.0.tgz
cd kafka_2.13-3.0.0

# start kafka environment
bin/zookeeper-server-start.sh config/zookeeper.properties > /dev/null &
bin/kafka-server-start.sh config/server.properties > /dev/null &
bin/kafka-topics.sh --create --topic test --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 > /dev/null
bin/kafka-topics.sh --create --topic train --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 > /dev/null

cd ..

python train_producer.py &
python test_producer.py &
python train_consumer.py

# terminate kafka environment
echo 'terminate kafka environment'
rm -rf /tmp/kafka-logs /tmp/zookeeper
rm -rf *.tgz*
rm -rf kafka_2.13-3.0.0
