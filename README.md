
### run pip local
```
python3 -m venv myvenv
source myvenv/bin/activate
pip install -r requirements.txt
```

### run pip ubuntu
https://www.digitalocean.com/community/tutorials/how-to-install-the-django-web-framework-on-ubuntu-18-04
```
python3.6 -m venv my_env
source my_env/bin/activate
pip install -r requirements.txt 
```

### ubuntu run pip
```
https://www.digitalocean.com/community/tutorials/how-to-install-the-django-web-framework-on-ubuntu-18-04
```
kafka-topics --create --topic test2 --partitions 3 --zookeeper zoo1:2181 --replication-factor 1 Created topic test2

bin/kafka-topics.sh --describe --topic test2 --bootstrap-server 54.91.38.33:9092

bin/kafka-topics.sh --describe --topic test2 --bootstrap-server localhost:9092




bin/kafka-topics.sh --create --topic test3 --bootstrap-server 54.91.38.33:9092


bin/kafka-console-producer.sh --topic test2 --bootstrap-server 54.91.38.33:9092
bin/kafka-console-producer.sh --topic test2 --bootstrap-server localhost:9092

bin/kafka-console-consumer.sh --topic test2 --from-beginning --bootstrap-server 54.91.38.33:9092


advertised.listeners=PLAINTEXT://ec2-54-91-38-33.compute-1.amazonaws.com:9092









