import os
import json
import numpy as np
from kafka import KafkaProducer, KafkaConsumer
from punk.feature_selection.rf import rfregressor_feature_selection



def convert_dict_of_np_to_lists(bunch):
    for k, v in bunch.items():
        if isinstance(v, np.ndarray):
            bunch[k] = v.tolist()
    return bunch


def process_msg(msg):
    # Load in msg
    data = json.loads(msg)
    data["X"] = np.array(data["X"])
    data["y"] = np.array(data["y"])

    # Run primitive
    output = rfregressor_feature_selection(data["X"], data["y"])

    # Prepare output for producer
    output = convert_dict_of_np_to_lists(output)
    return json.dumps(output)


if __name__=="__main__":
    # Connect to Kafka via env vars
    kafka_server  = os.environ.get("KAFKASERVER", "kafka:9092")
    consumerTopic = os.environ.get("CONSUMERTOPIC", "consumer")
    producerTopic = os.environ.get("PRODUCERTOPIC", "producer")
    assert(kafka_server is not None)
    assert(consumerTopic is not None)
    assert(producerTopic is not None)

    # Create producer and consumer
    consumer = KafkaConsumer(consumerTopic, bootstrap_servers=[kafka_server])
    producer = KafkaProducer(bootstrap_servers=kafka_server)
    for msg in consumer:
        # Read incoming msg
        incomingMsg = msg.value.decode('utf-8')
        
        # process incomgin msg and produce outgoing msg
        outgoing = process_msg(incomingMsg)

        with open("client_test.txt", "w") as f:                                 
            f.write(incomingMsg + '\n')

        # Send outgoing msg
        outgoingMsg = producer.send(producerTopic, outgoing.encode('utf-8'))

    producer.flush()

