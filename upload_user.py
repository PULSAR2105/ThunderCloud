# -*- coding: utf-8 -*-
import socket
from tqdm import tqdm
import math
import time
import sys
import os

def upload_user() :
    host = "127.0.0.1" # ip adresse per example : 127.0.0.1 is loclhost
    port = 12803
    
    #Connection with the other user : 
    connection_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #--------------------------------
    
    #We test if the remote server is reachable : 
    try :
    	connection_server.connect((host, port))
    	print("Connection made with the server : \nport : " + str(port) + "\nip : " + str(host) + "\n")
    except :
    	print("A error occured, Connection not made with the server.\nStopping of programm...")
    	time.sleep(3)
    	connection_server.close()
    	sys.exit()
    #-------------------------------------------
    
    #Request the name of the file to be sent :
    file_existence = False
    while file_existence == False :
    	name_file = ""
    	while name_file == "" :
    		name_file = input(">> The path of file to send : \n> ")
    		if name_file == "" :
    			print("Error = The name of file is empty.\n")
    
    	try :
    		file = open(name_file, "r")
    		file.close()
    		file_existence = True
    	except:
    	    print("Error = The file '" + name_file + "' cannot be found.\n")
    #------------------------------------------
    
    #Recovery of size of file :	    
    octets = os.path.getsize(name_file)
    #--------------------------
    
    #Display of file size : 
    print(">> Ok : '" + name_file + "' [", end=" ")
    
    if octets < 1024 :
    	print(str(octets) + " o]")
    
    elif octets < 1048576 :
    	print(str(round(octets / 1024, 2)) + "Ko]")
    
    elif octets < 1073741824 :
    	print(str(round(octets / 1048576, 2)) + "Mo]")
    
    else :
    	print(str(round(octets / 1073741824, 2)) + "Go]")
    #----------------------
    
    print(time.strftime(">> [%H:%M] Your upload will start."))
    
    #Send of name and size of file :
    msg_infos = "NAME " + name_file.split("/")[-1] + "SIZE " + str(octets)
    msg_infos = msg_infos.encode("utf-8")
    connection_server.send(msg_infos) # Envoi du nom et de la taille du fichier  
    #-------------------------------
    
    answer = connection_server.recv(1024)
    
    #Send of file :
    if answer == b"GO" :
        print(time.strftime(">> [%H:%M] Download is current..."))
    
        nb = 0
        file = open(name_file, "rb")
    
        if octets > 1024 :	# If the file is heavier than 1024 it is sent per packet
            for i in tqdm(range(math.ceil(octets / 1024))) :        		
                file.seek(nb, 0) #o ne moves in relation to the character number (from 1024 to 1024 bytes)
                data = file.read(1024) # Reading the file in 1024 bytes                            
                connection_server.send(data) # Sending the file per 1024 byte packet
                nb += 1024
    
            file.close()
            print(time.strftime(">> [%H:%M] Download complete."))
            connection_server.send(b"finished")
    
        else: # If not, we all go at once
            data = file.read()
            connection_server.send(data)
            file.close()
            print(time.strftime(">> [%H:%M] Download complete."))
            connection_server.send(b"finished")
    #--------------
    
    print(time.strftime(">> [%H:%M] Closing connection..."))
    time.sleep(3)
    connection_server.close()
