#Equipment Data Generation
Data Generation for the equipment stream analytics

## Prerequisite
1. [Python 3.8.5](https://www.python.org/downloads/release/python-385/)
2. [Docker](https://www.docker.com/)   
3. [Confluent Kafka 6.2.0](https://docs.confluent.io/platform/current/quickstart/ce-docker-quickstart.html)
Python Packages Required :
   confluent_kafka,kafka,kafka-python,requests,avro
##Setup
Configure the config.properties

For creating mock avro records (Equipment Mock Streams)
```
python equipmentProduce.py
```
For creating meta json records (Meta Update Streams)
```
python equipmentConsume.py
```

##Schema Evolution
For schema evolution change the config.properties to match the upgraded schema
```
equipment-value-schema=equipment-value-upgrade.avsc
mock_data=equipment-upgrade-mock
```