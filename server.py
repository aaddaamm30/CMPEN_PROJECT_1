####################################################
#
#   File        : server.py
#
#   Author      : Adam Loo
#   Created     : 04-10-2017
#   Last Edited : Thu 12 Oct 2017 09:57:24 PM EDT
#
#   Project     : CMPEN Web Server and Client
#   Goal        : Server process
#   Description : Will use the relevent python
#		  libraries to implement a web
#		  server that displays a simple 
#		  index page in HTML. 
#
####################################################

import socket
import sys
from thread import *

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print(s)

server = 'adampaulloo.com'
port = 80
server_ip = socket.gethostbyname(server)

try:
    s.bind((server_ip,port))
except socket.error as e:
    print(str(e))

s.listen(5)

def threaded_client(conn):
    conn.send(str.encode('Welcome, type  your info\n'))

    while True:
        data = conn.recv(2048)
        reply = 'Server output: ' + data.decode('utf-8')
        if not data:
            break
        conn.sendall(str.encode(reply))
    conn.close()

while True:

    conn, addr = s.accept()
    print('connected to: '+addr[0]+':'+str(addr[1]))
       
    start_new_thread(threaded_client,(conn,))
