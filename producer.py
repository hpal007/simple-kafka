from confluent_kafka import Producer
import uuid
import json

producer_config = {"bootstrap.servers": "localhost:9092"}
producer = Producer(producer_config)

order = {"order_id": str(uuid.uuid4()), "user": "alice", "item": "book", "quantity": 2}

value = json.dumps(order).encode("utf-8")


def delivery_report(err, msg):
    if err is not None:
        print(f"❌ Delivery failed: {err}")
    else:
        print(f"✅ Delivered to {msg.topic()},{msg.value()}")


producer.produce(topic="orders", value=value, callback=delivery_report)

producer.flush()  # Ensure all messages are sent before exiting
