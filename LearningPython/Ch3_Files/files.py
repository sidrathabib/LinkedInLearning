#use print("messages...") to debug your solution 

import os 

show_expected_result = False
show_hints = False

def file_info(): 
    totalbytes = 0
    folder = "deps"
    #get a list of all the files in the current directory 
    dirlist = os.listdir(folder)
    for entry in dirlist:
        #make sure its a file
        if os.path.isfile(folder + "/" + entry) and entry.endswith(".txt"):
            #add the file size to the total 
            filesize = os.path.getsize(folder + "/" + entry)
            totalbytes += filesize

if __name__ == "__file_info__":
    file_info()