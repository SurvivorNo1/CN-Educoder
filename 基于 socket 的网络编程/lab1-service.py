# -*- coding: utf-8 -*-
# @Time    : 2022/8/1 10:19
# @Author  : 陈玉辉
# @File    : service.py
import socket

HOST = "127.0.0.1"  # 在右侧补充代码， 本地主机,指这台计算机,对应的 IP 地址为 127.0.0.1
PORT = 5000  # 端口 0~1024 为系统保留
ADDRESS = (HOST, PORT)
BUFFER = 1024  # 数据发送和接收的最大数据大小

print("初始化服务器主机套接字对象.....")
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  # 在括号内补充代码， 面向网络的套接字: 通过 网络进行数据交互, TCP 协议,server 就是 socket 的实例
print("绑定主机信息....")

server.bind(ADDRESS)  # 元组,相当于一个参数
server.listen(10)

print("wait client")
conn, addr = server.accept()
while True:
    # 在下方补充代码，获取消息
    recvmsg = conn.recv(BUFFER)
    data = recvmsg.decode("utf-8")
    print("收到来自客户端的消息: ", data)
    if data == "exit":
        break
    # 在下方补充代码，发送消息
    conn.send(data.encode())

server.close()
