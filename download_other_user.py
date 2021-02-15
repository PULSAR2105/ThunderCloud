# -*- coding: utf-8 -*-
import threading 
import socket
import math
import time
import sys
import os

#DOWNLOAD : 

#To receiving a file from another user :
def query_download_other_user(client, infos_client) :
    #Opening of log file :
    log = open("logs/download_other_user.txt", "a")
    #---------------------

    #Recovery of connection informations :
    ip = infos_client[0]
    port = str(infos_client[1])
    log.write(time.strftime("[%H:%M] Server instance ready for " + ip + " : " + port + "\n"))
    #-------------------------------------

    #Recovery of file informations :
    received = ""
    received = client.recv(1024)
    info_received = received.decode("utf-8")
    
    name_file = info_received.split("NAME ")[-1]
    name_file = name_file.split("SIZE ")[0]
    octets = info_received.split("SIZE ")[1]
    octets = int(octets)
    
    log.write(time.strftime("[%H:%M] Ok : '" + name_file + "' ["))
    #-----------------------------

    #Display of file size :
    if octets < 1024 :
        log.write(str(octets) + " o]\n")
    
    elif octets < 1048576 :
        log.write(str(round(octets / 1024, 2)) + " Ko]\n")
    										
    elif octets < 1073741824 :
        log.write(str(round(octets / 1048576, 2)) + " Mo]\n")
    										
    else :
        log.write(str(round(octets / 1073741824, 2)) + " Go]\n")                        
    #----------------------    

    #start signal of download :
    log.write(time.strftime("[%H:%M] The download will be start.\n"))
    client.send(b"GO")
    log.write(time.strftime("[%H:%M] Download is current...\n"))
    #--------------------------

    #Downloading another user’s file :
    file = open("datas/" + name_file, "wb")
    
    while (client) :
        received = ""
        received = client.recv(1024)
    
        if received == b"finished" :        
            file.close()
            log.write(time.strftime("[%H:%M] Download is complete.\n"))
            break 

        elif not received : 
        	break                                    
                
        else : 
            file.write(received)             
    #---------------------------------

    #Closing connection :
    log.write(time.strftime("[%H:%M] Closing connection with " + ip + " : " + port + "\n"))
    log.close()
    client.close()
    #--------------------

#Starting of server for receipt another user's file :
def download_other_user() :
    #Starting of server :
    host = ""
    port = 12804
    threads_clients = []

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    log = open("logs/download_other_user.txt", "a")
    log.write(time.strftime(">> [%d/%m/%y - %H:%M] The server listen on the port : " + str(port) + "\n"))
    log.close()
    #--------------------

    #Acceptance of new connections :
    while True :
        client, infos_client = server.accept()
        threads_clients.append(threading.Thread(None, query_download_other_user, None, (client, infos_client), {}))
        threads_clients[-1].start()
    #-------------------------------
