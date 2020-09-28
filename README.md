
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
### run api
```
python producer.py
python consumer.py
```


### ubuntu run pip
```
https://www.digitalocean.com/community/tutorials/how-to-install-the-django-web-framework-on-ubuntu-18-04
```
### share code
```
sshfs ubuntu@ec2-54-91-224-152.compute-1.amazonaws.com:/home/ubuntu/code ~/kafka_research/producer -o IdentityFile=~/kindom/demo.pem -o allow_other
```


##### kill port 
```
sudo lsof -i -P -n | grep LISTEN
kill -9 id
```


#### BootstrapBrokerStringTls
b-1.awskafkatutorialclust.bwvs6a.c10.kafka.us-east-1.amazonaws.com:9094,b-2.awskafkatutorialclust.bwvs6a.c10.kafka.us-east-1.amazonaws.com:9094,b-3.awskafkatutorialclust.bwvs6a.c10.kafka.us-east-1.amazonaws.com:9094


###### produce
./kafka-console-producer.sh --broker-list BootstrapBrokerStringTls --producer.config client.properties --topic AWSKafkaTutorialTopic

```
./kafka-console-producer.sh --broker-list b-1.awskafkatutorialclust.bwvs6a.c10.kafka.us-east-1.amazonaws.com:9094,b-2.awskafkatutorialclust.bwvs6a.c10.kafka.us-east-1.amazonaws.com:9094,b-3.awskafkatutorialclust.bwvs6a.c10.kafka.us-east-1.amazonaws.com:9094 --producer.config client.properties --topic AWSKafkaTutorialTopic
```

###### consumer
./kafka-console-consumer.sh --bootstrap-server BootstrapBrokerStringTls --consumer.config client.properties --topic AWSKafkaTutorialTopic --from-beginning
```
./kafka-console-consumer.sh --bootstrap-server b-1.awskafkatutorialclust.bwvs6a.c10.kafka.us-east-1.amazonaws.com:9094,b-2.awskafkatutorialclust.bwvs6a.c10.kafka.us-east-1.amazonaws.com:9094,b-3.awskafkatutorialclust.bwvs6a.c10.kafka.us-east-1.amazonaws.com:9094 --consumer.config client.properties --topic AWSKafkaTutorialTopic --from-beginning
```






