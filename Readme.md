# Equipment Data Generation
Data Generation for the equipment stream analytics

[![CodeQL](https://github.com/appuv/KafkaDataGen/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/appuv/KafkaDataGen/actions/workflows/github-code-scanning/codeql) [![License](https://img.shields.io/github/license/appuv/KafkaDataGen)](https://github.com/appuv/KafkaDataGen/blob/master/LICENSE) [![GitHub top language](https://img.shields.io/github/languages/top/appuv/KafkaDataGen)]([https://github.com/appuv/KafkaDataGen](https://img.shields.io/github/languages/top/appuv/KafkaDataGen))

## Prerequisite
1. [Python 3.8.5](https://www.python.org/downloads/release/python-385/)
2. [Docker](https://www.docker.com/)   
3. [Confluent Kafka 6.2.0](https://docs.confluent.io/platform/current/quickstart/ce-docker-quickstart.html)

Python Packages Required :

   confluent_kafka,kafka,kafka-python,requests,avro

## Setup
Configure the config.properties

For creating mock avro records (Equipment Mock Streams)
```
python equipmentProduce.py
```
For creating meta json records (Meta Update Streams)
```
python equipmentConsume.py
```

## Schema Evolution
For schema evolution change the config.properties to match the upgraded schema
```
equipment-value-schema=equipment-value-upgrade.avsc
mock_data=equipment-upgrade-mock
```

## Further Reading
[Medium](https://medium.com/@masterappu/realtime-temperature-analytics-using-kafka-b1db9d91b870)

## Demo
[Youtube](https://youtu.be/Cj3BeA4bV1c)
