# Docker Compose Setup Guide

This document explains the Kafka Docker Compose configuration using Confluent's KRaft mode (Kafka without Zookeeper).

## 🐳 Service Configuration

### Kafka Service
- **Image**: `confluentinc/cp-kafka:7.8.3` - Confluent's official Kafka image
- **Container Name**: `kafka` - Easy reference for Docker commands
- **Port Mapping**: `9092:9092` - Exposes Kafka broker on localhost:9092

## 🔧 Environment Variables Explained

### KRaft Mode Configuration
| Variable | Development | Production | Purpose |
|----------|-------------|------------|---------|
| `KAFKA_KRAFT_MODE` | `true` | `true` | Enables KRaft mode (no Zookeeper needed) |
| `CLUSTER_ID` | `kafka-cluster-1` | `prod-kafka-cluster` | Unique cluster identifier |
| `KAFKA_NODE_ID` | `1` | `1,2,3` (per broker) | Unique node ID in the cluster |

### Process Roles
| Variable | Development | Production | Purpose |
|----------|-------------|------------|---------|
| `KAFKA_PROCESS_ROLES` | `broker,controller` | `broker,controller` | Node acts as both broker and controller |
| `KAFKA_CONTROLLER_QUORUM_VOTERS` | `1@kafka:9093` | `1@kafka-1:9093,2@kafka-2:9093,3@kafka-3:9093` | Controller election participants |
| `KAFKA_CONTROLLER_LISTENER_NAMES` | `CONTROLLER` | `CONTROLLER` | Listener name for controller communication |

### Network & Communication
| Variable | Development | Production | Purpose |
|----------|-------------|------------|---------|
| `KAFKA_LISTENERS` | `PLAINTEXT://0.0.0.0:9092, CONTROLLER://0.0.0.0:9093` | `SASL_SSL://0.0.0.0:9092, CONTROLLER://0.0.0.0:9093` | Internal listener addresses |
| `KAFKA_ADVERTISED_LISTENERS` | `PLAINTEXT://localhost:9092` | `SASL_SSL://kafka-1:9092` | Address clients use to connect |

### Storage & Replication
| Variable | Development | Production | Purpose |
|----------|-------------|------------|---------|
| `KAFKA_LOG_DIRS` | `/tmp/kafka-combined-logs` | `/opt/kafka/logs` | Directory for Kafka logs |
| `KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR` | `1` | `3` | Replication factor for offset topic |

### Production-Only Variables
| Variable | Value | Purpose |
|----------|-------|---------|
| `KAFKA_HEAP_OPTS` | `"-Xmx3G -Xms3G"` | JVM memory allocation |
| `KAFKA_DEFAULT_REPLICATION_FACTOR` | `3` | Default topic replication |
| `KAFKA_MIN_INSYNC_REPLICAS` | `2` | Minimum replicas for writes |
| `KAFKA_SECURITY_INTER_BROKER_PROTOCOL` | `SASL_SSL` | Secure broker communication |
| `KAFKA_SSL_KEYSTORE_LOCATION` | `/etc/kafka/secrets/kafka.keystore.jks` | SSL certificate store |
| `KAFKA_JMX_PORT` | `9999` | Monitoring port |

## 💾 Volume Configuration

- **Volume Name**: `kafka_kraft`
- **Mount Point**: `/var/lib/kafka/data`
- **Purpose**: Persists Kafka data across container restarts

## 🚀 Usage Commands

```bash
# Start the Kafka cluster
docker-compose up -d

# Check container status
docker-compose ps

# View logs
docker-compose logs kafka

# Stop the cluster
docker-compose down

# Stop and remove volumes (⚠️ deletes all data)
docker-compose down -v
```

## 🔍 Key Differences from Traditional Setup

1. **No Zookeeper**: Uses KRaft mode for metadata management
2. **Single Node**: Simplified setup for development/learning
3. **Combined Roles**: Same node serves as broker and controller
4. **Minimal Replication**: Factor of 1 (suitable for single-node setup)

## 📝 Notes

- This setup is designed for **development and learning** purposes
- For production, use the production values shown in the environment variables tables above
- The `PLAINTEXT` protocol means **no encryption** - fine for local development
- Production requires minimum 3 brokers, SSL certificates, and persistent storage