####################################################
#
#   File        : client.py
#
#   Author      : Adam Loo
#   Created     : 04-10-2017
#   Last Edited : Thu 12 Oct 2017 05:43:01 PM EDT
#
#   Project     : CMPEN Web server and client
#   Goal        : Client requests HTML doc
#   Description : Requests and displays HTML doc
#		  from server.py
#
####################################################

#command line that reads url from command line
#and uses HTTP protocol to process a request to
#specified URL

import * from socket

def make_http(procol, url, port, fh):
    user_input = input('URL: ')
    procol, rest = user_input.split('://')
    
    
