
### run pip shell
```
python3 -m venv myvenv
source myvenv/bin/activate
pip install -r requirements.txt
```


kafka-topics --create --topic test2 --partitions 3 --zookeeper zoo1:2181 --replication-factor 1 Created topic test2

bin/kafka-topics.sh --describe --topic test2 --bootstrap-server 54.91.38.33:9092

bin/kafka-topics.sh --describe --topic test2 --bootstrap-server localhost:9092




bin/kafka-topics.sh --create --topic test3 --bootstrap-server 54.91.38.33:9092


bin/kafka-console-producer.sh --topic test2 --bootstrap-server 54.91.38.33:9092
bin/kafka-console-producer.sh --topic test2 --bootstrap-server localhost:9092

bin/kafka-console-consumer.sh --topic test2 --from-beginning --bootstrap-server 54.91.38.33:9092








