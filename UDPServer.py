####################################################
#
#   File        : UDPServer.py
#
#   Author      : Adam Loo
#   Created     : 07-10-2017
#   Last Edited : Sat 07 Oct 2017 02:24:26 AM EDT
#
#   Project     : CMPEN web client and server
#   Goal        : Work with given solutions
#   Description : Bruh honestly IM so h igh right
#				  now. les see this work doe. 
#				  not gonana lie would bone a doe 
#				  probabaly. kaf;ljsda;lsdkfj
#
####################################################

#thjslhelhelhlshldhhhjb

from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("The server is ready to receive")
while True:
	message, clientAddress = serverSocket.recvfrom(2048)
	modifiedMessage = message.decode().upper()
	serverSocket.sendto(modifiedMessage.encode(), clientAddress)
