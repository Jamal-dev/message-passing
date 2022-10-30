import time
from concurrent import futures
import logging
import json
import os
from kafka import KafkaProducer
# from confluent_kafka import Producer
import socket
conf = {"bootstrap.servers": "kafka-service:9092", 
        "client.id": socket.gethostname()}

import grpc

import location_pb2
import location_pb2_grpc

TOPIC_NAME = os.environ["KAFKA_TOPIC"]
KAFKA_SERVER = os.environ["KAFKA_URL"]
# TOPIC_NAME = "test"
# KAFKA_SERVER = "my-release-kafka.default.svc.cluster.local:9092"
# KAFKA_SERVER = "kafka-service:9092"

logging.info("Kafka topic: %s", TOPIC_NAME)
logging.info("Kafka server: %s", KAFKA_SERVER)
producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)
# producer = Producer(conf)

class Location(location_pb2_grpc.LocationServiceServicer):
    def Create(self, request, context):
        request_value = {
            'id': int(request.id),
            'longitude': int(request.longitude),
            'latitude': int(request.latitude)
        }
        logging.info('request entity ', request_value)
        # Turn order_data into a binary string for Kafka
        kafka_data = json.dumps(request_value).encode()
        logging.info('kafka_data ', kafka_data)
        # Send the data to Kafka
        producer.send('location', kafka_data)
        # producer.produce("test", 
        #                 key="message", 
        #                 value=request_value)
        return location_pb2.LocationMessage(**request_value)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    location_pb2_grpc.add_LocationServiceServicer_to_server(Location(), server)
    server.add_insecure_port('[::]:5000')
    server.start()
    logging.info("Server started")
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)
