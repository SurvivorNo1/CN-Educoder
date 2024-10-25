# UDPPingerServer.py 
from socket import * 

########## Begin ##########

serverSocket = socket(AF_INET, SOCK_DGRAM) 
serverSocket.bind(("0.0.0.0",12000))
########## End ##########

print( serverSocket)
