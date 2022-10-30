from kafka import KafkaConsumer
import logging
import os
import json
from sqlalchemy import create_engine

KAFKA_SERVER = os.environ["KAFKA_URL"]
TOPIC_NAME = os.environ["KAFKA_TOPIC"]
# TOPIC_NAME = "test"
# KAFKA_SERVER = "my-release-kafka.default.svc.cluster.local:9092"

# KAFKA_SERVER = "kafka-service:9092"

# database credentials
DB_USERNAME = os.environ["DB_USERNAME"]
DB_PASSWORD = os.environ["DB_PASSWORD"]
DB_HOST = os.environ["DB_HOST"]
DB_PORT = os.environ["DB_PORT"]
DB_NAME = os.environ["DB_NAME"]

# DB_USERNAME = "ct_admin"
# DB_PASSWORD = "d293aW1zb3NlY3VyZQ=="
# DB_HOST = "postgres"
# DB_PORT = "5432"
# DB_NAME = "geoconnections"

logging.info("Kafka topic: %s", TOPIC_NAME)
logging.info("Kafka server: %s", KAFKA_SERVER)

print("Kafka topic: %s", TOPIC_NAME)
print("Kafka server: %s", KAFKA_SERVER)

consumer = KafkaConsumer(TOPIC_NAME, bootstrap_servers=[KAFKA_SERVER])

def save_db(location):
    
    id = int(location["id"])
    latitude, longitude = int(location["latitude"]), int(location["longitude"])
    table_insert = f'''INSERT INTO 
                       location (person_id, coordinate) VALUES 
                       ({id}, ST_Point({latitude}, {longitude}))'''

    logging.debug(f"insert command: {table_insert}")
    try:
        conn = create_engine(f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}", echo=True)
        cur = conn.cursor()
        cur.execute(table_insert)
        cur.close()
    except Exception as error:
        logging.error(f"{error}")
    finally:
        if conn is not None:
            conn.close()




for topic in consumer:
    location_message = json.loads(topic.value.decode())
    logging.debug (f'location_message = {location_message}')
    save_db(location_message)