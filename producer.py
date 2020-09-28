from kafka_api import KafkaClass
import time
import json

ts =  str( int( time.time() ) )

data_dic = {
    "seesion_id": ts,
    "base64": "asdg44tfghfg33...",
    "name": "0000"
}

data = json.dumps(data_dic)
#data= b'111111'
KafkaClass().producer(data)