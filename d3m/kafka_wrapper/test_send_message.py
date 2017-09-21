import os
from kafka import KafkaProducer, KafkaConsumer
from json import JSONDecoder, JSONEncoder
import sys


def addKeyToJSON(msg, key, value):
    decoder = JSONDecoder()
    encoder = JSONEncoder()
    jsonMsg = decoder.decode(msg)

    jsonMsg[key] = value 

    return encoder.encode(jsonMsg)


if __name__=="__main__":
    # Connect to Kafka via env vars
    kafka_server  = "192.168.7.3:9092"
    consumerTopic = "feature_selection_input"
    producerTopic = "feature_selection_results"
    assert(kafka_server is not None)
    assert(consumerTopic is not None)
    assert(producerTopic is not None)

    producer = KafkaProducer(bootstrap_servers=kafka_server)

    msg = "{}"

    msg = addKeyToJSON(msg, 'id', '23')
    msg = addKeyToJSON(msg, 'path', sys.argv[1])

    producer.send(consumerTopic, msg.encode('utf-8'))

    producer.flush()

    print("Sent to " + str(consumerTopic))
    

