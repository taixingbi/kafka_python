
from kafka import KafkaProducer
from kafka import KafkaConsumer

from kafka.errors import KafkaError
import time
import json

class KafkaClass:
    def __init__(self):
        print("\n--------------------------Kafka--------------------------")
        #self.ip= '54.91.38.33'
        self.ip= 'ec2-54-91-38-33.compute-1.amazonaws.com'
        
        #self.ip= 'localhost'
        self.bootstrap_servers= [self.ip+':9092',self.ip+':9093', self.ip+':9094']
        #self.bootstrap_servers= [ '54.91.38.33:9092', '54.91.38.33:9093', '54.91.38.33:9094']

        self.topic= 'test'
        print('bootstrap_servers: ', self.bootstrap_servers)
        print('topic: ', self.topic)

    def producer(self, data):
        print("producer..")
        producer = KafkaProducer(bootstrap_servers= self.bootstrap_servers )

        topic= self.topic
        print(data)

        producer = KafkaProducer(value_serializer=lambda m: json.dumps(m).encode('ascii'))

        producer.send(topic, data)

        # -------------------read to send -------------------
        producer.flush()

        #print(topic, dataJson)

        return topic, data

    def consumer(self):
        print("consumer..")


        # To consume latest messages and auto-commit offsets
        consumer = KafkaConsumer(self.topic,
                                group_id='my-group',
                                bootstrap_servers= self.bootstrap_servers)
        for message in consumer:
            print("\n--------------consumer-------------")
            print('bootstrap_servers: ', self.bootstrap_servers)
            print('topic: ', self.topic)
                    # message value and key are raw bytes -- decode if necessary!
            # e.g., for unicode: `message.value.decode('utf-8')`

            # print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
            #                                     message.offset, message.key,
            #                                     message.value))
            
            topic= message.topic 
            b= message.value
     
            dataStr = b.decode('utf8').replace("'", '"')

            data = json.loads(dataStr) # str2json
            print(data)

            print("consumer done")


if __name__ == "__main__": 

    ts =  str( int( time.time() ) )

    data = {
        "seesion_id": ts,
        "base64": "asdg44tfghfg33...",
        "name": "0000"
    }
    data_json = json.dumps(data)
    KafkaClass().producer(data_json)
    #KafkaClass().consumer()


        

        