####################################################
#
#   File        : server_2.py
#
#   Author      : Adam Loo
#   Created     : 12-10-2017
#   Last Edited : Fri 13 Oct 2017 01:18:46 AM EDT
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

#http parsing funciton to get appropreate reponse file
def getHTMLRsp(msg):
    
    #split the message
    http_vars = msg.split()
    print("[HTTP ANALYSIS]\n"+str(http_vars))
    
    #identify if get
    if str(http_vars[0]) != "GET":
        
        #open read and close a bad request html page
        fh = open("./bad_request.html","r")
        bad_request_response = fh.read()
        fh.close()

        #return string of html description
        return bad_request_response

    #if index requested
    elif str(http_vars[1]) == "/index.html":
        
        #open read and close index html page
        fh = open("./index.html","r")
        index = fh.read()
        fh.close

        #return string of index html
        return index

    #case file not found and 'GET' used
    else:
        
        #open read and close not found html page
        fh = open("./not_found.html", "r")
        not_found = fh.read()
        fh.close()

        #return 404 not found
        return not_found

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

            #get http_message
            print("[SERVER] reading into http_message")
            http_message = conn.recv(2096)
            
            #use http parsing function to get appropreat response
            #handled by getHTMLRsp
            sendback = getHTMLRsp(http_message.decode())

            #helpfull output
            print("[SERVER] returning:")
            print(str(sendback))

            #format header
            conn.send("HTTP/1.0 200 OK\n".encode())
            conn.send("Content-Type: text/html\n".encode())
            conn.send("\n".encode()) #empty line to indicate beginning of data
            #encode html response
            conn.send(sendback.encode())

            #close socket
            conn.close()

        except IOError:
            print("[SERVER] ERROR")

    #close server socket
    s.close()

#main function call
if __name__ == "__main__":
    Main()
