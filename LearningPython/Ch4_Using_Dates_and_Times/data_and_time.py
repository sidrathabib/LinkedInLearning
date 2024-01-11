show_expected_result = False
show_hints = False

def count_days(theyear, themonth, whichday): 
    import calendar 
    daycount = 0
    weekslist = calendar.monthcalendar(theyear, themonth)
    #monthcalendar returns an array of week lists, like this 
    # [
    # [0, 0, 1, 1, 1]
    # [1, 1, 1, 1, 1]
    # [1, 1, 1, 1, 1]
    # [1, 1, 1, 1, 1]
    # [1, 1, 1, 0, 0]
    # ]

    for week in weekslist: 
        if week[whichday] != 0: 
            daycount += 1
        return daycount
    
# calling and testing cases
# testyear = 2025
# testmonth = 12
# testday = 0
# result = Answer.count_days(testyear, testmonth, testday)