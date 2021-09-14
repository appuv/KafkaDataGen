import configparser
import json
from kafka import KafkaProducer


def publish_data():
    config = configparser.ConfigParser()
    config.read("resources/config.properties")

    producer = KafkaProducer(bootstrap_servers=config.get('kafka','bootstrap.servers'))

    topic=config.get('kafka','equipment_topic_json')
    input_data = open(config.get('kafka','equipment_json_mock_data'))
    lines_data = input_data.readlines()
    for line in lines_data:
        key=json.loads(line.strip().split("|")[0])
        value = json.loads(line.strip().split("|")[1])
        try:
            producer.send(topic,key=key,value=value)
        except Exception as e:
            print(f"Exception while producing record value - {key} and {value} to topic {topic}: {e}")
        else:
            print(f"Successfully produced - {key}  and {value} to topic {topic}")
    producer.flush()

if __name__=="__main__":
    publish_data()
