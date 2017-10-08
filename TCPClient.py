####################################################
#
#   File        : TCPClient.py
#
#   Author      : Adam Loo
#   Created     : 07-10-2017
#   Last Edited : Sat 07 Oct 2017 08:09:22 PM EDT
#
#   Project     : Honestly I just love man
#   Goal        : try not to come through this gay
#   Description : holy shit if anyone reads this. 
#				  SERIOUSLy for the fact that this
#				  is all on github wtf. not hyet tho
#				  I give myself a 3/5 for getting
#				  to the bouldering wall. idk im
#				  pretty drunk. ok tcplcient niga
#
####################################################

from socket import *

serverName = "127.0.0.1"

serverPort = 11345
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
sentence = raw_input('Input lowercase sentence you itch ass nigga: ')
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print('what is good period: ', modifiedSentence.decode())
clientSocket.close()



