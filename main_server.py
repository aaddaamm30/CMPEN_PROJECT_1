####################################################
#
#   File        : main_server.py
#
#   Author      : Adam Loo
#   Created     : 08-10-2017
#   Last Edited : Thu 12 Oct 2017 05:38:53 PM EDT
#
#   Project     : CMPEN web server and client
#   Goal        : return an index page
#   Description : Uses TCP style connection to
#		  handle each server request one at
#		  a time, returns an HTML index page
#
####################################################

#import socket lib
from socket import *

#setting port and loading socket object
serverPort = 8080
serverSocket = socket(AF_INET,SOCK_STREAM)

#testing for serversocket type
print(type(serverSocket))

#binding our socket to our port and ip
serverSocket.bind(('',serverPort))

#listening for requests from clients
serverSocket.listen(True)

print('[server] initialized \n[server] listening')

while True:

    #establising connection
    connectionSocket, addr = serverSocket.accept()
   
    #get HTTP message
    HTTP_message = connectionSocket.recv(msgleg)
    
    #section from textbook
    sentence = connectionSocket.recv(1024).decode()
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence.encode())
    connectionSocket.close()


