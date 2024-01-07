#ERRORS
#x = 10 / 0

# a seperate section of code to group them together 
try: 
    x = 10/0
except: 
    print("Well that didn't work!")

#you can also catch speciic exceptions 
try: 
    answer = input("what should i divide 10 by")
    num = int(answer)
    print(10/num)
except ZeroDivisionError as e: 
    print("you cant divide by 0")
except ValueError as e: 
    print("you didnt give me a valid number")
    print(e)
finally: 
    print("this code always runs")