#import socket module
from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM) 
#Prepare a sever socket 
serverSocket.bind(("127.0.0.1",6789))
serverSocket.listen(1)

#while True:
print('开始WEB服务...')

try:
    connectionSocket, addr = serverSocket.accept()
    message = connectionSocket.recv(1024) # 获取客户发送的报文
    #读取文件内容
    ######### Begin #########
    message = message.decode("utf-8")
    line1 = message.split("\n")[0]
    url = line1.split()[1]
    fo = open(f".{url}","r+")
    outputdata = fo.read()
    ######### End #########
    print(outputdata)
    connectionSocket.close()
except IOError:
        
    connectionSocket.close()
serverSocket.close()