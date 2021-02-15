# -*- coding: utf-8 -*-
import socket
from tqdm import tqdm
import math
import time
import sys
import os

host = ''
port = 12801

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(5)
print("The server listen on the port : " + str(port))

connection_client, infos_connection = server.accept()

received = ""
received = connection_client.recv(1024)
info_received = received.decode("utf-8")

name_file = info_received.split("NAME ")[-1]
name_file = name_file.split("SIZE ")[0]
name_file = name_file.split("/")[-1]
octets = info_received.split("SIZE ")[1]
octets = int(octets)

print(time.strftime(">> [%H:%M] Ok : '" + name_file + "' ["), end=" ")

if octets < 1024 :
    print(str(octets) + " o]")

elif octets < 1048576 :
    print(str(round(octets / 1024, 2)) + " Ko]")
										
elif octets < 1073741824 :
    print(str(round(octets / 1048576, 2)) + " Mo]")
										
else :
    print(str(round(octets / 1073741824, 2)) + " Go]")                        

print(time.strftime(">> [%H:%M] The download will be start."))
connection_client.send(b"GO")
print(time.strftime(">> [%H:%M] Download is current..."))

file = open(name_file, "wb")

pbar = tqdm(total=math.ceil(octets / 1024))

while (connection_client) :
    received = ""
    received = connection_client.recv(1024)

    if not received : 
    	pbar.close()
    	break                                    
       
    if received == b"finished" :
        pbar.close()
        file.close()
        print(time.strftime(">> [%H:%M] Download is complete."))
            
    else : 
        file.write(received)   
        pbar.update(1)

print(time.strftime(">> [%H:%M] Closing connection..."))
time.sleep(3)
connection_client.close()
main_connection .close()
