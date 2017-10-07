####################################################
#
#   File        : UDPClient.py
#
#   Author      : Adam Loo
#   Created     : 07-10-2017
#   Last Edited : Sat 07 Oct 2017 02:24:28 AM EDT
#
#   Project     : CMPEN web client and server
#   Goal        : Expirement with textbook solution
#   Description : Textbook experimentation. Fully 
#				  the approach I take later with 
#				  use the tools found here. 
#
####################################################

#most comments will be guesses at what the acutal 
#meaning of the line will be. im pretty high

#new lib
from socket import *

s_Name = "127.0.0.1"

s_Port = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = raw_input('Input lowercase scentence: ')
clientSocket.sendto(message.encode(),(s_Name, s_Port))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())
clientSocket.close()

