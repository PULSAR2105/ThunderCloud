# -*- coding: utf-8 -*-
import upload_other_user as uou
import download_user as du
import download_other_user as dou
import upload_user as uu
import threading 
import socket
import math
import time
import sys
import os

threads = []

def secondary0() :
    uou.upload_other_user()

def secondary1() : 
    uu.upload_user()

def secondary2() : 
    du.download_user()

def actions() :
    global threads
    while True :
        answer = input(">> What do you want ? \n>>'upload' \n>>'download' \n>")
        if answer  == "upload" :
            threads.append(threading.Thread(None, secondary1, None, (), {})) 
            threads[-1].start()
    
        elif answer == "download" :
            threads.append(threading.Thread(None, secondary2, None, (), {})) 
            threads[-1].start()
            threads[-1].join()

               
        else :
            print("Error : Your entry is invalid.")

threads.append(threading.Thread(None, actions, None, (), {}))
threads.append(threading.Thread(None, secondary0, None, (), {})) 
threads[0].start()
threads[1].start()
threads[0].join()