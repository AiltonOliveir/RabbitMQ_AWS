#Author       		: Ailton Oliveira
#Email          	: ailtonpoliveira01@gmail.com
import pika

credential = pika.PlainCredentials('user', 'password')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1', port=5672, credentials=credential))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World! Ailton Oliveira')
                      
print(" [x] Sent!! ")
connection.close()
