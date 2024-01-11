from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta 

#construct a basic timedelta and print it
print(timedelta(days=365, hours=5, minutes=1))

#print todays date
now = datetime.now()
print("today is", now)

#print todays date one year from now
print("one year from now it will be ", str(now + timedelta(days=365)))

#create a timedelta that uses more than one argument 
print("in two days and 3 days it will be", str(now + timedelta(weeks=2, days=3)))

#calculatre the date 1 week ago, formatted as a string
t = datetime.now() - timedelta(weeks=1)
s = t.strftime("%A %B %d, %Y")
print("one week ago it was", s)

#how many days until april fools day 
today = date.today()
afd = date(today.year, 4, 1)

#use date comparison to see if april fools has already gone for this year
#if it has, use the replace() function to get the date for next year 
if afd < today: 
    print("April fools day alrdy went by: ", ((today-afd).days))
    afd = afd.replace(today.year + 1)

#now calculate the amt of tiem until april fools day 
time_to_afd = afd - today 
print("it is", time_to_afd, "days untol the next april fools day ")