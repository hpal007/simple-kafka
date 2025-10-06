
Troubleshoot steps: 
- Getting into kafka container : `docker exec -it kafka bash`
- Checking number of topis : `kafka-topics --list --bootstrap-server localhost:9092`
- Check events metadata: 
    - `kafka-topics --bootstrap-server localhost:9092 --describe`
    - `kafka-topics --bootstrap-server localhost:9092 --describe --topic orders`



other commands -help
`kafka-topics --bootstrap-server localhost:9092 --help`

[kafka-docks](https://docs.confluent.io/kafka/operations-tools/kafka-tools.html)

# kafka-console-consumer
 - Use to consume records from a topic, It reads data from Kafka topics and outputs it to standard output.
`kafka-console-consumer --bootstrap-server localhost:9092 --topic orders --from-beginning`

`.poll(1.0)` 
    - Asks/poll the broker for any new messages on the subscribed topics and retruns them to the consumer for processing.
    - `1.0` indicate timeout in seconds

