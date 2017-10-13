####################################################
#
#   File        : server.py
#
#   Author      : Adam Loo
#   Created     : 04-10-2017
#   Last Edited : Thu 12 Oct 2017 08:44:22 PM EDT
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

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print(s)

server = 'adampaulloo.com'
port = 80

server_ip = socket.gethostbyname(server)
print(server_ip)

request = "GET / HTTP/1.1\nHost: "+server_ip+"\n\n"
s.connect((server,port))
s.send(request.encode())
result = s.recv(4096)

#print(result)

while(len(result) > 0):
    print(result)
    result = s.recv(4096)
    
