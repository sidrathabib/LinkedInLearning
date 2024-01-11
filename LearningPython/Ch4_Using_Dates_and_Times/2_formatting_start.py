from datetime import datetime 

def main(): 
    #times and dates can be formatted using a set of predefined string 
    # control codes
    now = datetime.now()

    #### date formatting ####
    # %y%Y - year // %a%A - weekday // %b%B - month // %d - day of month
    print(now.strftime("The current year is: %Y"))
    print(now.strftime("%a, %d %B, %y")) #wed, january 10, 24

    # %c -- locales date and time // %x - locales date, %X - time
    print(now.strftime("Locale date and time: %c"))
    print(now.strftime("Locale date: %x"))
    print(now.strftime("Locale time: %X"))


    # %I %H - 12/24 Hour // %M - minute, %S -- second, %p - locale's AM/PM
    print(now.strftime("current time: %I:%M:S% %P"))
    print(now.strftime("24-hr time: %H:%M"))

if __name__ == "__main__":
    main()