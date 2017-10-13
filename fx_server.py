####################################################
#
#   File        : fx_server.py
#
#   Author      : Adam Loo
#   Created     : 12-10-2017
#   Last Edited : Fri 13 Oct 2017 12:34:52 AM EDT
#
#   Project     : CMPEN server client
#   Goal        : youtube workthrough w/ functions
#   Description : python practice
#
####################################################

import socket

#main funciton
def Main():

    port = 80
    server = 'adampaulloo.com'
    #server_id = socket.gethostbyname(server)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    request = 'GET / HTTP/1.1\nHost: '+server+'\n\n'

    s.connect((server,port))
    s.send(request.encode())

    data = s.recv(2096)
    print(str(data.decode()))


if __name__ == '__main__':
    Main()
