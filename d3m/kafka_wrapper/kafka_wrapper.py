import os
from kafka import KafkaProducer, KafkaConsumer



def process_msg(msg):
    return "Hello World"


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

