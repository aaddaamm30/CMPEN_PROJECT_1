####################################################
#
#   File        : client.py
#
#   Author      : Adam Loo
#   Created     : 04-10-2017
#   Last Edited : Tue 17 Oct 2017 03:59:36 PM EDT
#
#   Project     : CMPEN Web server and client
#   Goal        : Client requests HTML doc
#   Description : Requests and displays HTML doc
#				  from server.py
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
	print(type(urlInfo))
	
	print(str(urlInfo))

	

#if driver of client 
if __name__ == "__main__":
	Main()    
