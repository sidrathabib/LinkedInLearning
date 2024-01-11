#import the calender module
import calendar

#create a plain text caleder
c = calendar.TextCalendar(calendar.MONDAY)
str = c.formatmonth(2022, 1, 0, 0)
print(str)

#create an html formatted calender
hc = calendar.HTMLCalendar(calendar.SUNDAY)
str = hc.formatmonth(2022, 1)
print(str)

#loop over the days of a momnth
#zeros mean that the day of the week is in an overlapping month
for i in c.itermonthdays(2022, 8):
    print(i)

#calender module privides useful utilities for the given locale
#such as names of days and months in both full and abbreviated forms
for name in calendar.month_name: 
    print(name)

for day in calendar.day_name: 
    print(day)

#calacualte days based on a rule for example consider
# a team meeting on the first friday of every month
# to fugure out what days that would be for each month
# we can use this script

print("Team meetigns will be on: ")
for m in range(1, 13):
    cal = calendar.monthcalendar(2022, m)
    weekone = cal[0]
    weektwo = cal[1]
    if weekone[calendar.FRIDAY] != 0:
        meetday = weekone[calendar.FRIDAY]
    else: 
        meetday = weektwo[calendar.FRIDAY]

    print(calendar.month_name[m], meetday)