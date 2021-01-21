from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')

while True:
    val = input("Enter your value: ") 
    print(val)
    producer.send('sample', str.encode(val))#or key=b'message-two', value=b''
    