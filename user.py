# -*- coding: utf-8 -*-
import download_upload_other_user as duou
import download_upload_user as duu
import threading 
import socket
import math
import time
import sys
import os

if __name__ == "__main__" :
    def main():
        query = False
        while query == False :
            if input(">> What do you want ? \n>>'upload' \n>>'download' \n>") == "upload" :
                query = True
        
            elif input(">> What do you want ? \n>>'upload' \n>>'download' \n>") == "upload" :
                query = True
        
            else :
                print("Error : Your entry is invalid.")

    def secondary0():
        duou.download_other_user()

threadA = threading.Thread(None, main, None, (), {}) 
threadB = threading.Thread(None, secondary0, None, (), {}) 
threadA.start() 
threadB.start()