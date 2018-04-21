#!/usr/bin/env python
# encoding: utf-8

'''
@author:maidou
@contact:QQ4113291000
@time:18/4/21.上午11:08
'''

'''
pip install pyzmq

req/rep (请求答复模式) 远程调用任务分配
pub/sub (订阅模式) 数据分发
push/pull (管道模式) 多任务并行

有效绑定对
PUB & SUB
REQ & REP
REQ & XREP
XREQ & XREP
XREQ & XREQ
XREP & XREP
PUSH & PULL
PAIR & PAIR

发送机制 是否COPY 两种  是否重复发送 发送数据是否保存内存  单消息限制在4M

格外标示 ZMQ_SNDMORE ZMQ_RCVMORE

s.recv(zmq.NOBLOCK) #非阻塞模式

混合接收模式
p = zmq.Poller() #工具
p.register(a, zmq.POLLIN)
p.register(b, zmq.POLLIN) #a , b 为 s

用法
while True:
    socks = dict(p.poll())
    if a in socks and socks[a] == zmq.POLLIN
        msg = a.recv()
    if b in socks and socks[b] == zmq.POLLIN
        msg = b.recv()
        
关闭
zmq.close()
zmq.term()

#大数据多包发送
more = s.getsockopt(zmq.RCRMORE)
if more
    s.send(msg, zmq.SNDMORE) 
    
    
代理模式 proxy a->b
msg = a.recv()
b.send(msg)

PROXY 

f = context.socket(zmq.XREP)
b = context.socket(zmq.XREQ)
f.bind('')
b.bind('')

p = zmq.Poller()
p.register(f, zmq.PULLIN)
p.register(b, zmq.PULLIN)

while True:
    socks = dict(p.poll())
    if socks.get(f) == zmq.POLLIN:
        msg = f.recv()
        more = f.getsockopt(zmq.RCVMORE)
        if more:
            b.send(msg, zmq.SNDMORE)
        else:
            b.send(msg)
    if socks.get(b) == zmq.POLLIN:
        msg = b.recv()
        more = b.getsockopt(zmq.RCVMORE)
        if more:
            f.send(msg, zmq.SNDMORE)
        else:
            f.send(msg)

代理方案
zmq.device(zmq.QUEUE, f, b) # f , b 是 s
f.close()
b.close()
context.term()

代理三种模式
应答模式 queue XREP/XREQ
订阅模式 forwarder SUB/PUB
分包模式 streamer PULL/PUSH

zmq.PAIR #分步骤处理  inproc://step* 为进程间通信准备

zmq 命名机制
p = context.socket(zmq.PUB)
p.send_multipart(['A','msg'])
p.send_multipart(['B','msg'])

s = context.socket(zmq.SUB)
s.setsockopt(zmq.SUBSCRIBE, 'B')

[address, contents] = s.recv_multipart()

zmq.IDENTITY
s.setsockopt(zmq.IDENTITY, 'HELLO')

#swap space bytes
p.setsockopt(zmq.HWM, 1) #高水位
p.setsockopt(zmq.SWAP, 25000000)


c = zmq.Context() #上下文 必须对象
s = c.socket(zmq.***) #连接方式 zmq.REP 经典服务端 zmq.PUB 发布消息 zmq.REQ 经典客户端 zmq.SUB 订阅端 zmq.PUSH 推送 zmq.PULL 拉取
s.bind('') #服务端绑定
s.connect('') #客户端连接
经典模式
s.send_pyobj(obj) #发送python 对象消息
s.recv_pyobj() #接收对象

订阅发布模式 PUB/SUB
s.send_pyobj([topic,obj]) #发布消息 topic 主题 obj 消息

接收设置
s.setsockopt(zmq.SUBSCRIBE,'') #接收ALL_TOPIC
订阅多个需要循环设定
s.setsockopt(zmq.SUBSCRIBE,topic) #接收TOPIC 消息
topic, msg = s.recv_pyobj() #接收对象 topic 和 msg 消息

PUSH/PULL 模式  没有消费者，消息不会消耗(发布者进程维护) 消息只能一个消费者获得
上游 任务发布
工人 中间，具体工作
下游 信号采集或者工作结果收集

上游
zmq.PUSH
s.send('') #发送数据

工人 recevier sender
zmq.PULL
recevier.recv() #s.recv() 接收数据
zmq.PUSH
sender.send('') #s.send('') 发送给下游

下游
zmq.PULL
recevier.recv() #s.recv() 接收数据


类型说明
REQ 负责主动提出请求、要求得到回复(严格同步)
REP 负责应答请求(不主动、严格同步)
XREQ 分销类型 负责对进出数据排序 均匀分发给接入的 REP或者XREP
XREP 路由类型 消息转发至任何连接地方

路由四种方式
XREP-to-XREQ
XREP-to-REQ
XREP-to-REP
XREP-to-XREP
'''

import zmq

c = zmq.Context()

s = c.socket(zmq.REP)

s.bind("ipc:///tmp/zmq")

while True:
    msg = s.recv_pyobj()
    s.send_pyobj(msg)

s.close()

if __name__ == '__main__':
    pass