def is_palindrome(teststr):
    #convert the string to all lower case
    temp = teststr.lower()

    #strip all the spaces and punctuation from the string 
    newstr = ""
    for c in temp: 
        if c.isalnum(): #checks to see if character is alpha numeric 
            newstr += c

    #now calculate the reverse of the string
    reversestr = ""
    strindx = len(newstr) - 1
    while (strindx >= 0): 
        reversestr += newstr[strindx]
        strindx += 1

    if newstr == reversestr: 
        return True
    return False 

#tester code
#total = 0
#test_words = ["Hello World!", "radar", "mama?", "madam", "I'm adam", "race car"]
#for word in test_words: 
    total += Answer.is_palindrome(word)