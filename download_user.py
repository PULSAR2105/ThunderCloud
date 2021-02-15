# -*- coding: utf-8 -*-
import threading 
import socket
import math
import time
import sys
import os

#Repatriation of the requested file :
def download_user() :   
    #Recovery the ip adresse of storage place :
    file_existence = False
    while file_existence == False :
        name_file = ""
        while name_file == "" :
            name_file = input(">> The name of file to send : \n> ")
            if name_file == "" :
                print("Error = The name of file is empty.\n")
    
        try :
            with open("paths/" + name_file + ".txt", "r") as file :
                line = file.readline()
                line = line.split(":")[1] # ip adresse of storage place 
                host = line.split(" ")[0]

            file.close()
            file_existence = True
        except:
            print("Error = The file '" + name_file + "' cannot be found.\n")
    #------------------------------------------

    port = 12801

    #Connection with the other user : 
    connection_other_user = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #--------------------------------

    #We test if the remote server is reachable :
    try :
        connection_other_user.connect((host, port))
        print("Connection made with the server : \nport : " + str(port) + "\nip : " + str(host) + "\n")
    except :
        print("A error occured, Connection not made with the server.\nStopping of programm...")
        time.sleep(3)
        connection_other_user.close()
    #-------------------------------------------

    """   
    
    octets = os.path.getsize(name_file)
    
    print(">> Ok : '" + name_file + "' [", end=" ")
    
    if octets < 1024 :
        print(str(octets) + " o]")
    
    elif octets < 1048576 :
        print(str(round(octets / 1024, 2)) + "Ko]")
    
    elif octets < 1073741824 :
        print(str(round(octets / 1048576, 2)) + "Mo]")
    
    else :
        print(str(round(octets / 1073741824, 2)) + "Go]")
    
    print(time.strftime(">> [%H:%M] Your upload will start."))
    
    msg_infos = "NAME " + name_file.split("/")[-1] + "SIZE " + str(octets)
    msg_infos = msg_infos.encode("utf-8")
    connection_server.send(msg_infos) # Envoi du nom et de la taille du fichier  
    
    answer = connection_server.recv(1024)
    
    if answer == b"GO" :
        print(time.strftime(">> [%H:%M] Download is current..."))
    
        nb = 0
        file = open(name_file, "rb")
    
        if octets > 1024 :  # Si le fichier est plus lourd que 1024 on l'envoi par paquet
            for i in tqdm(range(math.ceil(octets / 1024))) :                
                file.seek(nb, 0) # on se deplace par rapport au numero de caractere (de 1024 a 1024 octets)
                data = file.read(1024) # Lecture du fichier en 1024 octets                            
                connection_server.send(data) # Envoi du fichier par paquet de 1024 octets
                nb += 1024
    
            file.close()
            print(time.strftime(">> [%H:%M] Download complete."))
            connection_server.send(b"finished")
    
        else: # Sinon on envoi tous d'un coup
            data = file.read()
            connection_server.send(data)
            file.close()
            print(time.strftime(">> [%H:%M] Download complete."))
            connection_server.send(b"finished")
    
    print(time.strftime(">> [%H:%M] Closing connection..."))
    time.sleep(3)
    connection_server.close()
    """
