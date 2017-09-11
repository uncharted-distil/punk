import os
from kafka import KafkaProducer, KafkaConsumer
from punk.feature_selection import *
import pandas
from json import JSONDecoder, JSONEncoder


def addKeyToJSON(msg, key, value):
    decoder = JSONDecoder()
    encoder = JSONEncoder()
    jsonMsg = decoder.decode(msg)

    jsonMsg[key] = value 

    return encoder.encode(jsonMsg)


def getFrameFromMessage(msg):
    decoder = JSONDecoder()
    jsonMsg = decoder.decode(msg)

    path = jsonMsg['path']

    frame = pandas.read_csv(path)

    return frame



def processPca(msg):
    try:
        frame = getFrameFromMessage(msg)
    except:
        return addKeyToJSON(msg, 'error', 'An error has occurred processing this message')

    pca = PCAFeatures()

    pca.fit("matrix", frame.values)

    results = pca.transform()

    return addKeyToJSON(msg, 'features', results)


def attachKafkaListenerToPrimitive(kafka_server, consumer_topic, producer_topic, process_msg):
    # Create producer and consumer
    consumer = KafkaConsumer(consumer_topic, bootstrap_servers=[kafka_server])
    producer = KafkaProducer(bootstrap_servers=kafka_server)
    for msg in consumer:
        # Read incoming msg
        incomingMsg = msg.value.decode('utf-8')
        
        # process incomgin msg and produce outgoing msg
        outgoing = process_msg(incomingMsg)

        # Send outgoing msg
        outgoingMsg = producer.send(producer_topic, outgoing.encode('utf-8'))

    producer.flush()
    


if __name__=="__main__":
    # Connect to Kafka via env vars
    kafka_server  = os.environ.get("KAFKASERVER")
    consumerTopic = os.environ.get("CONSUMERTOPIC")
    producerTopic = os.environ.get("PRODUCERTOPIC")
    assert(kafka_server is not None)
    assert(consumerTopic is not None)
    assert(producerTopic is not None)

    attachKafkaListenerToPrimitive(kafka_server, consumer_topic, producer_topic, processPca)
