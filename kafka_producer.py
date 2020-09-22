
from kafka import KafkaProducer
from kafka import KafkaConsumer

from kafka.errors import KafkaError
import time

import json

class KafkaClass:
    def __init__(self):
        print("\nKafkaCore...")
        self.bootstrap_servers= ['localhost:9092']
        self.topic= 'test'
        print('bootstrap_servers: ', self.bootstrap_servers)
        print('topic: ', self.topic)

    def producer(self, data):
        print("\nproducer..")
        producer = KafkaProducer(bootstrap_servers= self.bootstrap_servers )
        topic= self.topic

        producer = KafkaProducer(value_serializer=lambda m: json.dumps(m).encode('ascii'))
        producer.send(topic, data)

        # -------------------read to send -------------------
        producer.flush()

        #print(topic, dataJson)

        return topic, data

    def consumer(self):
        print("\nconsumer..")

        # To consume latest messages and auto-commit offsets
        consumer = KafkaConsumer(self.topic,
                                group_id='my-group',
                                bootstrap_servers= self.bootstrap_servers)
        for message in consumer:
            print("\n -----------------consumer message-----------------")
            # message value and key are raw bytes -- decode if necessary!
            # e.g., for unicode: `message.value.decode('utf-8')`

            # print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
            #                                     message.offset, message.key,
            #                                     message.value))
            
            topic= message.topic 
            print("topic ", topic)

            b= message.value
            print(b)
     
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
    print(data_json)

    KafkaClass().producer(data_json)
    #KafkaClass().consumerJson()


        

        
