####################################################
#
#   File        : main_server.py
#
#   Author      : Adam Loo
#   Created     : 08-10-2017
#   Last Edited : Thu 12 Oct 2017 10:37:04 PM EDT
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
serverHost = '127.0.0.1'

#testing for serversocket type
print(type(serverSocket))

#binding our socket to our port and ip
serverSocket.bind((serverHost,serverPort))

#listening for requests from clients
serverSocket.listen(1)

print('[server] initialized \n[server] listening\n')

while True:

    #establising connection
    connectionSocket, addr = serverSocket.accept()
  
    print('Connection from '+str(addr))
    
    data = connectionSocket.recv(2096)
    
    if not data:
        break

    print('from connected user: '+str(data))
    data = str(data).upper
    print 'sending: ' str(data)
   
    connectionSocket.send(data)
    c.close()


   #get HTTP message
    
   """ 
    HTTP_message = connectionSocket.recv(msgleg)
    
    #section from textbook
    sentence = connectionSocket.recv(1024).decode()
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence.encode())
    connectionSocket.close()

    """
