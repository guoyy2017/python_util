#!/usr/bin/env python
# encoding: utf-8

'''
@author:maidou
@contact:QQ4113291000
@time:18/4/21.下午2:47
'''

'''
rabbitmq client
pip install pika
https://blog.csdn.net/fgf00/article/details/52872730



Broker：简单来说就是消息队列服务器实体。 
Exchange：消息交换机，它指定消息按什么规则，路由到哪个队列。 
Queue：消息队列载体，每个消息都会被投入到一个或多个队列。 
Binding：绑定，它的作用就是把exchange和queue按照路由规则绑定起来。 
Routing Key：路由关键字，exchange根据这个关键字进行消息投递。 
vhost：虚拟主机，一个broker里可以开设多个vhost，用作不同用户的权限分离。 
producer：消息生产者，就是投递消息的程序。 
consumer：消息消费者，就是接受消息的程序。 
channel：消息通道，在客户端的每个连接里，可建立多个channel，每个channel代表一个会话任务
'''

import pika

# #连接队列服务器
# connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
# channel = connection.channel()
#
# #创建队列。有就不管，没有就自动创建
# channel.queue_declare(queue='hello')
#
# #使用默认的交换机发送消息。exchange为空就使用默认的
# channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
# print(" [x] Sent 'Hello World!'")
# connection.close()


#测试代码
import time
credential = pika.PlainCredentials('yyg','seek1234')
conn = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.0.199',virtual_host='/coin',credentials=credential))
channel = conn.channel()
channel.queue_declare(queue='hello', durable=True)
channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
time.sleep(20)
conn.close()
if __name__ == '__main__':
    pass