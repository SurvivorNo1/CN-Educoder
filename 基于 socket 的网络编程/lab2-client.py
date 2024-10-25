import socket

# 定义要连接的服务器信息
HOST =  "127.0.0.1"  # 在右侧补充代码，获取本地主机,指这台计算机,对应的 IP 地址为 127.0.0.1
PORT = 5001  # 端口 0~1024 为系统保留
ADDRESS = (HOST, PORT)
BUFFER = 1024  # 数据发送和接收的最大缓冲区大小
# 创建客户端套接字对象
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)   # 在括号内补充代码，相当于声明 socket 类型,同时生成 socket 链接对象,面向网络的套接字: 通过网络进行数据交互, UDP
client.settimeout(2)
msgs = ["hello services", "I'm client", "exit"]
for msg in msgs:
    # 在下方补充代码， 给服务器发送消息
    msg = msg.encode()
    client.sendto(msg,(HOST,PORT))
    # 在下方补充代码， 接收服务端信息
    recvmsg, addr = client.recvfrom(BUFFER)
    data = recvmsg.decode("utf-8")
    print('收到服务端的发来的消息: ', data)
client.close()
