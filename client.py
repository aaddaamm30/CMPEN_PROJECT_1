####################################################
#
#   File        : client.py
#
#   Author      : Adam Loo
#   Created     : 04-10-2017
#   Last Edited : Tue 17 Oct 2017 10:26:02 PM EDT
#
#   Project     : CMPEN Web server and client
#   Goal        : Client requests HTML doc
#   Description : Requests and displays HTML doc
#                 from server.py
#
####################################################

#command line that reads url from command line
#and uses HTTP protocol to process a request to
#specified URL

#libraries including urlparse
from socket import *
from urllib.parse import urlparse

#main function   
def Main():
	
    #print startup status
    print('[CLIENT] initializing ...')
    user_input = input('[CLIENT] URL: ')

    #use urlparse function
    urlInfo = urlparse(user_input)

    #initiating connection
    clientSocket = socket(AF_INET, SOCK_STREAM)

    print('[CLIENT] connecting ...')

    #testing if port number specified
    if urlInfo.port != None:
        print(urlInfo.hostname)
        print(urlInfo.port)
        clientSocket.connect((urlInfo.hostname, urlInfo.port))
    else:
        print(urlInfo.hostname)
        clientSocket.connect((urlInfo.hostname, 80))

    #formatting http request
    message = 'GET '+urlInfo.path+' HTTP/1.1\n\n'

    print('[CLIENT] HTTP MESSAGE:\n'+message)
    
    #sending request
    clientSocket.send(message.encode())

    #get response
    response = clientSocket.recv(2048)

    print(response.decode())




    

#if driver of client 
if __name__ == "__main__":
    Main()    
