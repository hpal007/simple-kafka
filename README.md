
# Simple Kafka Learning Project

A minimal Kafka producer-consumer example for learning Kafka fundamentals with Python and Docker.

## 📁 Codebase Structure

```
├── docker-compose.yaml    # Kafka cluster setup (single broker with KRaft)
├── producer.py           # Kafka producer - sends order events
├── tracker.py           # Kafka consumer - processes order events  
├── pyproject.toml       # Python dependencies (confluent-kafka)
└── README.md           # This file
```

## 🚀 Quick Start

1. **Start Kafka**: `docker-compose up -d`
2. **Send orders**: `uv run producer.py`
3. **Track orders**: `uv run tracker.py`

## 🔧 Key Components

- **Producer** (`producer.py`): Generates order events with UUID, user, item, and quantity
- **Consumer** (`tracker.py`): Subscribes to "orders" topic with consumer group "order_tracker"
- **Kafka Cluster**: Single broker setup using Confluent's KRaft mode (no Zookeeper)

## 🛠️ Troubleshooting Commands

```bash
# Access Kafka container
docker exec -it kafka bash

# List topics
kafka-topics --list --bootstrap-server localhost:9092

# Describe topics
kafka-topics --bootstrap-server localhost:9092 --describe --topic orders

# Console consumer (view messages)
kafka-console-consumer --bootstrap-server localhost:9092 --topic orders --from-beginning

# Help
kafka-topics --bootstrap-server localhost:9092 --help
```

## 📚 Resources

- [Kafka Tools Documentation](https://docs.confluent.io/kafka/operations-tools/kafka-tools.html)

