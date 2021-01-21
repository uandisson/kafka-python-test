from kafka import KafkaConsumer


while True:
    print('init')
    consumer = KafkaConsumer('sample')
    
    for message in consumer:
        print('Received message: {}'.format(message.value.decode()))
