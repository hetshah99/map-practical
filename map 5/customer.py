import psycopg2
import pika, os
import time

#INPUT
cid = input("Enter customer ID : ")
cname = input("Enter customer name : ")
cmed = input("Enter medicine name that you want : ")
cquant = input("Enter medicine quantity required : ")
print("Let us check the stock ! Order pending !")
#DATABASE POSTGRESQL
connection = psycopg2.connect(user="postgres",
                                  password="het",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="postgres")
cursor = connection.cursor()
cursor.execute("ROLLBACK")

postgres_insert_query = """ INSERT INTO customer (CID,CAME,CMED,CQUANT ) VALUES (%s,%s,%s,%s)"""
record_to_insert = (cid,cname,cmed,cquant)
cursor.execute(postgres_insert_query, record_to_insert)
connection.commit()
if(connection):
    cursor.close()
    connection.close()

#RABBITMQ PUBLISH QUEUE1
url = os.environ.get('CLOUDAMQP_URL', 'amqps://ugsynvns:zl-xQ-7yv9OHkXk9s7BQizgUBGBSzTff@fox.rmq.cloudamqp.com/ugsynvns')
params = pika.URLParameters(url)
connection2 = pika.BlockingConnection(params)
channel = connection2.channel()
channel.queue_declare(queue='queue1')

channel.basic_publish(exchange='',
                      routing_key='queue1',
                      body=cquant
                      )
connection2.close()

#RABBITMQ SUBSCRIBE QUEUE2
time.sleep(15)
url = os.environ.get('CLOUDAMQP_URL', 'amqps://ugsynvns:zl-xQ-7yv9OHkXk9s7BQizgUBGBSzTff@fox.rmq.cloudamqp.com/ugsynvns')
params = pika.URLParameters(url)
connection2 = pika.BlockingConnection(params)
channel = connection2.channel()
channel.queue_declare(queue='queue2')

method_frame, header_frame, body = channel.basic_get(queue = 'queue2')
print(body)
print("Status about your order : ", body)      
channel.basic_ack(delivery_tag=method_frame.delivery_tag)
connection2.close()
 

