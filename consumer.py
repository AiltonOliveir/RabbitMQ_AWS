#Author       		: Ailton Oliveira
#Email          	: ailtonpoliveira01@gmail.com
import requests
import pika

def callback(ch, method, properties, body):
    print(body)
    print('\n')
    

def receive():
    credential = pika.PlainCredentials('user', 'password')
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1', port=5672, credentials=credential))
    channel = connection.channel()

    channel.queue_declare(queue='hello')
    
    channel.basic_consume('hello',callback,auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
        
    
if __name__ == '__main__':
    receive()
    
