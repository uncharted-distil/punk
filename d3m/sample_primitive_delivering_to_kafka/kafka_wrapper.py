import os
import json
import numpy as np
from kafka import KafkaProducer, KafkaConsumer
from punk.feature_selection import RFFeatures



def process_msg(msg):
    # Load in msg
    data = json.loads(msg)
    data["X"] = np.array(data["X"])
    data["y"] = np.array(data["y"])

    # Run primitive
    rf = RFFeatures(problem_type="regression", cv=3,                    
                    scoring="r2", verbose=0, n_jobs=1)               
    rf.fit(("matrix", "matrix"), (data["X"], data["y"]))                          
    indices = rf.transform()

    # Prepare output for producer
    return json.dumps(indices.tolist())


if __name__=="__main__":
    # Connect to Kafka via env vars
    kafka_server  = os.environ.get("KAFKASERVER")
    consumerTopic = os.environ.get("CONSUMERTOPIC")
    producerTopic = os.environ.get("PRODUCERTOPIC")
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

        # Send outgoing msg
        outgoingMsg = producer.send(producerTopic, outgoing.encode('utf-8'))

    producer.flush()

