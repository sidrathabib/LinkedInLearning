from datetime import date 
from datetime import time 
from datetime import datetime


def main(): 
    ## DATA OBJECTS 
    #get todays date from the simple today() method from the date class 
    today = date.today()
    print("Today's date is ", today)

    #print out the dates indivudual components 
    print("date componenets: ", today.day, today.month, today.year)
    
    #retrieve today's weekday (0=monday, 6=sunday)
    print("todays weekday # is: ", today.weekday())
    days = ["mon", "tues", "wed", "thurs", "fri", "sat", "sun"]
    print("which is a ", days[today.weekday()])

    ##datetime objects 
    #get todays date from the datetime class
    today = datetime.now()
    print("the current date and time is: ", today)

    #get the current time 
    t = datetime.time(datetime.now())
    print("the current time is: ", t)