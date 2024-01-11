#Basic data types in Python: numbers, strings, booleans, sequences, dictionaries

myint = 5
myfloat = 13.2 
mystr = "this is a string"
mybool = True
mylist = [0, 1, "two", 3.2, False]
mytuple = {0, 1, 2}
mydict = {"one" : 8, "two" : 2} #maps keys to sepcific values 

print(myint)
print(myfloat)
print(mystr)
print(mybool)
print(mylist)
print(mytuple)
print(mydict)

#redeclaring a variable works
myint = "abc"
print(myint) #comes up again at the end of printed stuff

#to access a member of a sequence type, use []
print(mylist[2])
print(mytuple[1])

#use slices to get parts of q sequence 
print(mylist[1:5])
print(mylist[1:5:2])#start, end, and step value aka skip every 2nd one

#you can use slices to reverse a sequence
print(mylist[::-1]) #default start, default end, and step value 

# dictionaries are acesed via keys
print(mydict["one"])

#ERROR: variables of different types cannot be combined
#print("string" + 123) --> 
print("string" + str(123))

#Global vs local variables in functions 
def someFunction(): 
    global mystr 
    mystr = "def" #prints copy alone without global
    print(mystr)

someFunction()
print(mystr)

del mystr #undefines variables in real time 
print(mystr)