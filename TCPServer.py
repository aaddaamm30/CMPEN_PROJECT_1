#
##################################################
#
#   File        : TCPServer.py
#
#   Author      : Adam Loo
#   Created     : 07-10-2017
#   Last Edited : Sat 07 Oct 2017 08:09:23 PM EDT
#
#   Project     : wheres ms right
#   Goal        : tony stark shit
#   Description :j;lkjlkjkkkjmnmlklkk
#
####################################################

from socket import *
serverPort = 11345
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print('The server is reat to recieve.  things are good')
while True:
	connectionSocket, addr = serverSocket.accept()
	sentence = connectionSocket.recv(1024).decode()
	capitalizedSentence = sentence.upper()
	connectionSocket.send(capitalizedSentence.encode())
	connectionSocket.close()
