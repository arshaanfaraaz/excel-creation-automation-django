import pika
import json
import random

def publish_message(message):
    params = pika.URLParameters('amqps://jgxvurpl:qGuR7GPKPPjg5qGfpj4xiYtxa17WhbxQ@octopus.rmq3.cloudamqp.com/jgxvurpl')
    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    channel.queue_declare(queue='my_queue')
    message = json.dumps(message)
    channel.basic_publish(
         exchange='',
         routing_key='my_queue',
         body=message
    )
    print(f'Message published {message}')
    connection.close()