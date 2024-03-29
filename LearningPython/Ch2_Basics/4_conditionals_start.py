def main(): 
    x, y = 10, 100

    #conditional flow uses if, elif, use
    if x < y: 
        result = "x is less than y"
    elif x == y: 
        result = "x is equal to y"
    else: 
        result = "x is greater than y"

    print(result)


    #conditional statements let you use a if C else b"
    result = "x is less than y" if x < y else "x is greater or equal to y"
    print(result)

    #match-case makes it easy to compare multiple values 
    value = "one"
    match value: 
        case "one":
            result = 1
        case "two":
            result = 2
        case "three" | "four":
            result = (3,4)
        case _: #default
            result = -1


def main(): 
    x = 10
    userIn = input("What is your num: ")

    #conditional flow uses if, elif, use
    if x < userIn: 
        result = "x is less than userIn"
    elif x == userIn: 
        result = "x is equal to userIn"
    else: 
        result = "x is greater than userIn"

    print(result)






if __name__ == "__main__":
    main()