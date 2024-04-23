echo "Waiting for Kafka to be ready..."
cub kafka-ready -b localhost:9092 1 20

TOPIC_NAME="finhub_data"
PARTITIONS=1
REPLICATION_FACTOR=1

echo "Creating Kafka topic: ${TOPIC_NAME}"
kafka-topics \
  --create \
  --if-not-exists \
  --zookeeper zookeeper:2181 \
  --partitions ${PARTITIONS} \
  --replication-factor ${REPLICATION_FACTOR} \
  --topic ${TOPIC_NAME}

echo "Kafka topic created: ${TOPIC_NAME}"
