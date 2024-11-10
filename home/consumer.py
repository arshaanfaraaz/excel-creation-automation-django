import pika
import pandas as pd
import json
import uuid

def generate_excel(message):
    message = json.loads(message)
    df = pd.DataFrame(message)
    df.to_excel(f"output_{uuid.uuid4()}.xlsx", index=False)



def call_back(ch, method, properties, body):
    message = body.decode()
    generate_excel(message)
    
    
params = pika.URLParameters('amqps://jgxvurpl:qGuR7GPKPPjg5qGfpj4xiYtxa17WhbxQ@octopus.rmq3.cloudamqp.com/jgxvurpl')
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='my_queue ')
channel.basic_consume(queue='my_queue', on_message_callback=call_back, auto_ack=True) 
print('consumer started: ')
channel.start_consuming()
