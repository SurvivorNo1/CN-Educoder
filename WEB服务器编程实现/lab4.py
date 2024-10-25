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
        filename = message.split()[1]       
		f = open(filename[1:])
		outputdata = f.read();
		
		#发送响应的头部信息
		header = ' HTTP/1.1 200 OK\nConnection: close\nContent-Type: text/html\nContent-Length: %d\n\n' % (len(outputdata))
	 	#########Begin#########
		connectionSocket.send(header.encode())
		#########End#########
       
        connectionSocket.close()
except IOError:
		
		connectionSocket.close()
serverSocket.close()