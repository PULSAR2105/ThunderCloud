# -*- coding: utf-8 -*-
import threading 
import socket
import math
import time
import sys
import os

#Repatriation of the requested file :
def query_download_user(client, infos_client) :
    #Recovery of connection informations :
    ip = infos_client[0]
    port = str(infos_client[1])
    print(time.strftime(">> [%H:%M] Server instance ready for " + ip + " : " + port))
    #-------------------------------------

    #Recovery of file informations :
    received = ""
    received = client.recv(1024)
    info_received = received.decode("utf-8")
    
    name_file = info_received.split("NAME ")[-1]
    name_file = name_file.split("SIZE ")[0]
    octets = info_received.split("SIZE ")[1]
    octets = int(octets)
    
    print(time.strftime(">> [%H:%M] Ok : '" + name_file + "' ["), end=" ")
    #-----------------------------

    #Display of file size :
    if octets < 1024 :
        print(str(octets) + " o]")
    
    elif octets < 1048576 :
        print(str(round(octets / 1024, 2)) + " Ko]")
    										
    elif octets < 1073741824 :
        print(str(round(octets / 1048576, 2)) + " Mo]")
    										
    else :
        print(str(round(octets / 1073741824, 2)) + " Go]")                        
    #----------------------    

    #start signal of download :
    print(time.strftime(">> [%H:%M] The download will be start."))
    client.send(b"GO")
    print(time.strftime(">> [%H:%M] Download is current..."))
    #--------------------------

    #Downloading user’s file :
    file = open(name_file, "wb")
    
    while (client) :
        received = ""
        received = client.recv(1024)
    
        if received == b"finished" :        
            file.close()
            print(time.strftime(">> [%H:%M] Download is complete."))
            break 

        elif not received : 
        	break                                    
                
        else : 
            file.write(received)             
    #--------------------------------------------------

    #Closing connection :
    print(time.strftime(">> [%H:%M] Closing connection with " + ip + " : " + port))
    client.close()
    #--------------------

def download_user() :
    host = ""
    port = 12800
    threads_clients = []

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(time.strftime(">> [%H:%M] The server 'download_user' listen on the port : " + str(port)))
    
    while True :
        client, infos_client = server.accept()
        threads_clients.append(threading.Thread(None, query_download_other_user, None, (client, infos_client), {}))
        threads_clients[-1].start()

