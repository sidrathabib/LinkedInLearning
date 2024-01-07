#define a basic function 
def func1(): #colon indicates we start scope or body of function 
    print("I am a function")

#function that takes arguments 
def func2 (arg1, arg2):
    print(arg1," ", arg2)

#function that returns values 
def cube(x): 
    return x * x * x

#function with default value for an arguemnet 
def power(num, x=1):
    result = 1; 
    for i in range(x):
        result = result * num #takes number and raises by given power 
    return result 

#function with variable number of arguments 
def multi_add(*args): #* means i can pass start number of var arguments
    result = 0        #* always has to be last
    for x in args: 
        result = result + x
        return result


func1() #prints, func gets directly run 
print(func1()) #called inside print statement 
print(func1) #none, would print definition of function value 

func2(10, 20) #prints 10 20
print(func2(10, 20)) #prints 10 20 and then none since theres no value
print(cube(3)) #prints 27

print(power(2)) #2 raised by 2
print (power(2,3)) #2 raised by 3
print(power(x=3, num=2))

print(multi_add(4,5,10,4))