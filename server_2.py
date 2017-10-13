####################################################
#
#   File        : server_2.py
#
#   Author      : Adam Loo
#   Created     : 12-10-2017
#   Last Edited : Thu 12 Oct 2017 10:52:47 PM EDT
#
#   Project     : CMPEN web server and client
#   Goal        : use appendex psudocode
#   Description : try to use the outline from the
#                 project description to develop
#                 the server.
#
####################################################

#import socket
from socket import *

#http parsing funciton to get file
def getFh(msg):
    #placeholder

#main function description
def Main():

    #make socket
    s = socket(AF_INET, SOCK_STREAM)

    #binding to port and host ('' = current location)
    port = 8080
    host = '127.0.0.1'
    s.bind((host, port))

    #open one channel and listen
    s.listen(1)

    #print status
    print("[SERVER] ... initializing")
    print("[SERVER] port: "+str(port))
    print("[SERVER] host: "+str(host))

    print("[SERVER] listening")

    #always be listeing
    while True:

        #when connection requested get client info
        conn, addr = s.accept()
        
        #print clinet info
        print("[SERVER] connection from : "+str(addr))
       
        conn.settimeout(10)
        print("[SERVER] TESTING")
        #catch errors
        try:

            print("[SERVER] reading into http_message")
            http_message = conn.recv(2096)
            print(str(http_message.decode()))

        except IOError:
            print("[SERVER] ERROR")

#main function call
if __name__ == "__main__":
    Main()
