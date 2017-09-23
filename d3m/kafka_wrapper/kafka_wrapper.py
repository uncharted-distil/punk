import os
import sys
from kafka import KafkaProducer, KafkaConsumer
from punk.feature_selection import PCAFeatures
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
        return addKeyToJSON(msg, 'error', sys.exc_info()[0])

    try:
        pca = PCAFeatures()

        pca.fit(["matrix"], frame.as_matrix())

        results = pca.transform()


        print(results)
        
        decoder = JSONDecoder()

        results['importance_on1stpc'] = decoder.decode(results['importance_on1stpc'])
        results['importance_onallpcs'] = decoder.decode(results['importance_onallpcs'])

        results = decoder.decode(results)


        return addKeyToJSON(msg, 'features', results)
    except:
        return addKeyToJSON(msg, 'error', sys.exc_info()[0])


def attachKafkaListenerToPrimitive(kafka_server, consumer_topic, producer_topic, process_msg):
    # Create producer and consumer
    consumer = KafkaConsumer(consumer_topic, bootstrap_servers=[kafka_server])
    producer = KafkaProducer(bootstrap_servers=kafka_server)
    print("Connected")
    for msg in consumer:
        # Read incoming msg
        print(msg)
        incomingMsg = msg.value.decode('utf-8')
        
        # process incomgin msg and produce outgoing msg
        outgoing = process_msg(incomingMsg)

        # Send outgoing msg
        outgoingMsg = producer.send(producer_topic, outgoing.encode('utf-8'))
        print(outgoing)

    producer.flush()
    


if __name__=="__main__":
    # Connect to Kafka via env vars
    kafka_server  = os.environ.get("KAFKASERVER")
    consumerTopic = os.environ.get("CONSUMERTOPIC")
    producerTopic = os.environ.get("PRODUCERTOPIC")
    assert(kafka_server is not None)
    assert(consumerTopic is not None)
    assert(producerTopic is not None)
    print(consumerTopic)

    attachKafkaListenerToPrimitive(kafka_server, consumerTopic, producerTopic, processPca)

