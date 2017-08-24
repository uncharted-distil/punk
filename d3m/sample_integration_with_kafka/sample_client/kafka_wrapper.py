import os
import json
import numpy as np
from sklearn import datasets
from kafka import KafkaProducer, KafkaConsumer



def convert_dict_of_np_to_lists(bunch):                                         
    for k, v in bunch.items():                                                  
        if isinstance(v, np.ndarray):                                           
            bunch[k] = v.tolist()                                               
    return bunch                                                                
                                                       

def prep_dataset():
    """ Prepare a dataset to be produced to a kafka topic
    and consequently consumed and properly process by a punk primitive.
    """
    data = dict()
    boston = datasets.load_boston()
    X, y = boston.data, boston.target
    X, y = X[::5], y[::5]
    data["X"], data["y"] = X, y
    data = convert_dict_of_np_to_lists(data)
    return json.dumps(data)


def process_msg(msg):
    # Load in msg
    data = json.loads(msg)
    data["X"] = np.array(data["X"])
    data["y"] = np.array(data["y"])

    # Run primitive
    output = rfclassifier_feature_selection(data["X"], data["y"])

    # Prepare output for producer
    output = convert_dict_of_np_to_lists(output)
    return json.dumps(output)


if __name__=="__main__":
    # Connect to Kafka via env vars
    kafka_server  = os.environ.get("KAFKASERVER", "kafka:9092")                   
    consumerTopic = os.environ.get("CONSUMERTOPIC", "consumer")                   
    producerTopic = os.environ.get("PRODUCERTOPIC", "producer")
    assert kafka_server is not None
    assert consumerTopic is not None 
    assert producerTopic is not None

    # Create producer and consumer
    consumer = KafkaConsumer(producerTopic, 
                             bootstrap_servers=[kafka_server],)
    producer = KafkaProducer(bootstrap_servers=kafka_server)
    
    # send test dataset to punk primitive
    outgoing = prep_dataset()
    outgoingMsg = producer.send(consumerTopic, outgoing.encode('utf-8'))
    producer.flush() 

    # wait for response
    for msg in consumer:
        # Read incoming msg
        incomingMsg = msg.value.decode('utf-8')

        print(incomingMsg)
        with open("client_test.txt", "w") as f:
            f.write(incomingMsg + '\n')
