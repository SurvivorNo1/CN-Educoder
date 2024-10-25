
from socket import *

########## Begin ##########
clientSocket =  socket(AF_INET, SOCK_DGRAM)  # 创建UDP套接字，使用IPv4协议
# 设置套接字超时值1秒
clientSocket.settimeout(1)
########## End ##########

print(clientSocket)
print(clientSocket.gettimeout())
