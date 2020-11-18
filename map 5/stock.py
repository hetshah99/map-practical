import psycopg2
import pika, os

#INPUT
mid = input("Enter medicine ID : ")
mname = input("Enter medicine name : ")
mquant = input("Enter medicine quantity : ")

#POSTGRESQL
connection = psycopg2.connect(user="postgres",
                                  password="het",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="postgres")
cursor = connection.cursor()
cursor.execute("ROLLBACK")

postgres_insert_query = """ INSERT INTO order1 (MID,MNAME,MQUANT ) VALUES (%s,%s,%s)"""
record_to_insert = (mid,mname,mquant)
cursor.execute(postgres_insert_query, record_to_insert)
#connection.commit()

#RABBITMQ SUBSCRIBE QUEUE1
url = os.environ.get('CLOUDAMQP_URL', 'amqps://ugsynvns:zl-xQ-7yv9OHkXk9s7BQizgUBGBSzTff@fox.rmq.cloudamqp.com/ugsynvns')
params = pika.URLParameters(url)
connection2 = pika.BlockingConnection(params)
channel = connection2.channel() # start a channel
channel.queue_declare(queue='queue1')

method_frame, header_frame, body = channel.basic_get(queue = 'queue1')
#print(body)      
channel.basic_ack(delivery_tag=method_frame.delivery_tag)
connection2.close() 

cquant=int(body)
print("Client ordered : ",cquant)

if(int(mquant)>cquant):
    mssg="Order Accepted !"
    mquant=int(mquant)-cquant
    print("Remaining stock :",mquant)
else:
    mssg="Order declined !"
print(mssg)
#RABBITMQ PUBLISH QUEUE2
url = os.environ.get('CLOUDAMQP_URL', 'amqps://ugsynvns:zl-xQ-7yv9OHkXk9s7BQizgUBGBSzTff@fox.rmq.cloudamqp.com/ugsynvns')
params = pika.URLParameters(url)
connection2 = pika.BlockingConnection(params)
channel = connection2.channel() # start a channel
channel.queue_declare(queue='queue2')

channel.basic_publish(exchange='',
                      routing_key='queue2',
                      body=mssg
                      )
connection2.close()
print("Order checked !")

#UPDATING STOCK AVAILABILITY
sql_update_query = """Update order1 set mquant = %s where mid = %s"""
cursor.execute(sql_update_query, (mquant, mid))
connection.commit()
if(connection):
    cursor.close()
    connection.close()
