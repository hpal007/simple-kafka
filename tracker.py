import json
from confluent_kafka import Consumer, KafkaError

consumer_config = {
    "bootstrap.servers": "localhost:9092",
    "group.id": "order_tracker",  # Group ID for the consumer of the orders topic
    "auto.offset.reset": "earliest",  # Start from the beginning if no offset is committed
}
consumer = Consumer(consumer_config)
consumer.subscribe(["orders"])  # Subscribe to the orders topic

try:
    print("🟢 Consumer is ready and waiting for new orders...")
    while True:
        msg = consumer.poll(1.0)  # Poll for messages with a timeout of 1 second
        if msg is None:
            continue
        if msg.error():
            print(f"❌ Error: {msg.error()}")
            continue

        value = msg.value().decode("utf-8")
        order = json.loads(value)

        print(
            f"📦 Received Order: {order['quantity']} x {order['item']} from {order['user']}"
        )

except KeyboardInterrupt:
    print("🔴 Exiting...")
finally:
    consumer.close()  # Close the consumer to commit final offsets and clean up
