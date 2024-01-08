import os 
from os import path 
import shutil
from shutil import make_archive
from zipfile import ZipFile

def main(): 
    #make a duplicate of an existing file 
    if path.exists("textfile.txt"):

        #get the path to the file in the current directory
        src = path.realpath("textfile.txt")

        #lets amke a backuo copy by appending "bak" to the name
        dst = src + ".bak"
        shutil.copy(src, dst)

        #rename the original file
        os.rename("textfile.txt", "newfile.txt")

        #now put things into a ZIP archive
        root_dir, tail = path.split(src)
        shutil.make_archive("archive", "zip", root_dir)

        #more fine grained control over zip files
        with ZipFile("testzip.zip", "w") as newzip:
            newzip.write("newfile.txt")
            newzip.write("textfile.txt.bak")


if __name__ == "__main__":
    main()