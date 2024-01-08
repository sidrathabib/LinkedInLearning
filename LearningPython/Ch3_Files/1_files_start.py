#bruh it didnt make the txt

def main(): 
    #open a file for writing and create it if it doesnt exist
    #myfile = open("textfile.txt", "w+") #write accesss, create file if it doesnt alrdy exist


    #open the file for appending text to the end
    myfile = open("textfile.txt", "a+") #append to file

    #write some lines of data to the file
    for i in range (10):
        myfile.write("This is some new text\n")

    #close the file when done 
    myfile.close()

    #seperately, comment out above
    #open the file back up and read the contents
    myfile = open("textfile.txt", "r") #read access
    if myfile.mode == 'r':
        contents = myfile.read()
        print(contents)
        #fl = myfile.readlines()
        #for x in fl: 
            #print(x)

if __name__ == "__main__": 
    main 