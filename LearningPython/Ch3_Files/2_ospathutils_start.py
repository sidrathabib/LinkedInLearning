#example file for wokring with os.path module

import os
from os import path 
import datetime
from datetime import date, time, timedelta
import time

def main(): 
    #print the name of the OS
    print(os.name)

    #check for item existence and type
    print("item exists: ", str(path.exists("textfile.txt"))) #checks if exists
    print("item is a file: ", path.isfile("textfile.txt")) #checks if its a file
    print("item is a directory: ", path.isdir("textfile.txt")) #check if its a directory 

    #work with file paths
    print("Item's path: ", path.realpath("textfile.txt")) #checks its path 
    print("Item's path and name: ", path.split(path.realpath("textfile.txt")))

    #get the modification time
    t = time.ctime(path.gettime("textfile.txt"))
    print(t) 
    print(datetime.datetime.fromtimestamp(path.gettime("textfile.txt")))

    #calculate how long ago the item was motified 
    td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.gettime("textfile.txt"))
    print("It has been", td, "since the file was modified")
    print("Or,", td.total_seconds(), "seconds")

    if __name__ == "__main__":
        main()