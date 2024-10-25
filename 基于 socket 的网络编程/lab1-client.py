# -*- coding: utf-8 -*-
# @Time    : 2022/8/1 10:19
# @Author  : 陈玉辉
# @File    : service.py
import socket

# 定义要连接的服务器信息
HOST = "127.0.0.1"  # 在右侧补充代码， 本地主机,指这台计算机,对应的 IP 地址为 127.0.0.1
PORT = 5000  # 端口 0~1024 为系统保留
ADDRESS = (HOST, PORT)
BUFFER = 1024  # 数据发送和接收的最大缓冲区大小 #创建客户端套接字对象
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)   # 在括号内补充代码， 相当于声明 socket 类 型,同时生成 socket 链接对象,面向网络的套接字: 通过网络进行数据交互, TCP #连接服务器
client.connect(ADDRESS)
infos = ["hello service", "I'm client", "exit"]
for info in infos:
    #在下方补充代码，发送信息
    client.send(info.encode())
    # 在下方补充代码， 接收服务端信息 print("等待服务端发送信息: ")
    data = client.recv(BUFFER)
    if data:
        print("收到服务端返回的数据：{}".format(data.decode("utf-8")))
client.close()
