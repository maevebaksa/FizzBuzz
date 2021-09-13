# FizzBuzzWuzz - Maeve Baksa - 2021

#the divisor values for the fizz, buzz and wuzz texts, more can be added by repeating the code from 
#the lines 19-21, changing the appended text and creating another variable here
fizzdiv = 3
buzzdiv = 5
wuzzdiv = 7

#set the start and stop value
value = 0
stopval = 100

#main loop
while value < stopval:

    #increase the number being checked by one
    value = value + 1
    #resets the numerical only check
    wastext=0
    #resets the printed string to blank
    string = ""
    
    #check to see if the value can be divided by the fizz value,
    #then append the word fizz to the the string, string
    #also set the wastext value to one, applicable later
    if (value % fizzdiv==0):
        string = string + "fizz"
        wastext = 1
    
    #check to see if the value can be divided by the buzz value
    if (value%buzzdiv==0):
        string = string + "buzz"
        wastext = 1
    
    #check to see if the value can be divided by the wuzz value
    if (value%wuzzdiv==0):
        string = string + "wuzz"
        wastext = 1
    
    #only print the numerical value if neither fizz, buzz or wuzz was triggered (as all of those)
    #set the wastext value to 1, which would make this line of code emitted.
    if wastext != 1:
        string = str(value)

    #print the finalized fuzz buzz wuzz :>
    print(string)