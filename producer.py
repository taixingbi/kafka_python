from kafka_api import KafkaClass
import time
import json

ts =  str( int( time.time() ) )

data = {
    "seesion_id": ts,
    "base64": "asdg44tfghfg33...",
    "name": "0000"
}

data_json = json.dumps(data)
KafkaClass().producer(data_json)