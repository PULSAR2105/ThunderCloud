import socket
import time
import sys
import os

host = ''
port = 12800

main_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
main_connection.bind((host, port))
main_connection.listen(5)
print("The server listen on the port : " + str(port))

connection_with_client, infos_connection = main_connection.accept()

received = ""
received = connection_with_client.recv(1024)
info_received = received.decode()

name_file = info_received.split("NAME ")[-1]
name_file = name_file.split("SIZE ")[0]
octets = info_received.split("SIZE ")[1]
octets = int(octets)

if octets < 1024 :
    print(time.strftime(">> [%H:%M] Ok : '" + name_file + "' [" + str(octets) + " o]"))

elif octets < 1048576 :
    print(time.strftime(">> [%H:%M] Ok : '" + name_file + "' [" + str(round(octets / 1024, 2)) + " Ko]"))
										
elif octets < 1073741824 :
    print(time.strftime(">> [%H:%M] Ok : '" + name_file + "' [" + str(round(octets / 1048576, 2)) + " Mo]"))
										
else :
    print(time.strftime(">> [%H:%M] Ok : '" + name_file + "' [" + str(round(octets / 1073741824, 2)) + " Go]"))                             

connection_with_client.send(b"GO")
print(time.strftime(">> [%H:%M] Download is current..."))

file = open(name_file, "wb")

while (connection_with_client) :
    received = ""
    received = connection_with_client.recv(1024)

    if not received : 
    	break                                    
       
    if received == b"BYE" :
        file.close()
        print(time.strftime(">> [%H:%M] Download is complete"))
            
    else : 
        file.write(received)   

print(time.strftime(">> [%H:%M] Closing connection..."))
time.sleep(3)
connection_with_client.close()
main_connection .close()
