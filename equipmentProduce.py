from confluent_kafka.avro import AvroProducer
from confluent_kafka import avro
import configparser
import json

def data_gen_from_file(key_schema,value_schema):
    return avro.load(key_schema),avro.load(value_schema)

def publish_data():
    config = configparser.ConfigParser()
    config.read("resources/config.properties")

    producer_config={
        "bootstrap.servers":config.get('kafka','bootstrap.servers'),
        "schema.registry.url":config.get('kafka','schema.registry.url')
    }
    key_schema,value_schema = data_gen_from_file(config.get('avro','equipment-key-schema'),config.get('avro','equipment-value-schema'))
    topic = config.get('kafka','topic')
    producer = AvroProducer(producer_config,default_key_schema=key_schema,default_value_schema=value_schema)

    input_data = open(config.get('kafka','mock_data'))
    lines_data = input_data.readlines()
    for line in lines_data:
        key=json.loads(line.strip().split("|")[0])
        value = json.loads(line.strip().split("|")[1])
        try:
            producer.produce(topic=topic, key=key, value=value)
        except Exception as e:
            print(f"Exception while producing record value - {key} and {value} to topic {topic}: {e}")
        else:
            print(f"Successfully produced - {key} and {value} to topic {topic}")
    producer.flush()

if __name__=="__main__":
    publish_data()
