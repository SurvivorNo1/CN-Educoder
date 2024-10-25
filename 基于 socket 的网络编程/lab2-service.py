# -*- coding: utf-8 -*-
import socket

# 定义服务器信息
print('初始化服务器主机信息')
HOST = "127.0.0.1" # 在右侧补充代码，获取本地主机,指这台计算机,对应的 IP 地址为 127.0.0.1
PORT = 5001  # 端口 0~1024 为系统保留
ADDRESS = (HOST, PORT)
BUFFER = 1024  # 数据发送和接收的最大缓冲区大小
# 创建 UDP 服务 socket 对象
print("初始化服务器主机套接字对象......")
server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  # 在括号内补充代码， 面向网络的套接字: 通过网络进行数据交互, UDP 协议,server 就是 socket 的实例
# 在下方补充代码 绑定主机信息
server.bind(ADDRESS)
print('绑定的主机信息......')
# 等待连接
print('等待客户端连接')
while True:
    recvmsg, addr = server.recvfrom(BUFFER) # 在右侧补充代码，获取返回信息
    data = recvmsg.decode("utf-8")
    print("收到来自客户端的消息: ", data)
    server.sendto(recvmsg,addr)     # 在右侧补充代码，发送信息
    if data == "exit":
        break
server.close()