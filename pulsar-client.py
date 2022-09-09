import pulsar

client = pulsar.Client('pulsar://localhost:6650')
consumer = client.subscribe('dns_topic', subscription_name='dns123')

while True:
    msg = consumer.receive()
    print(msg)
    print("Received message: '%s'" % msg.data())
    consumer.acknowledge(msg)

client.close()
