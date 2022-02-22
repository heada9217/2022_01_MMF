name = ""
count = 0 
MAX_TICKETS = 5 

while name != "xxx" and count < MAX_TICKETS:

    if count != 4:
        print ("You have {} seats " "left ".format(MAX_TICKETS - count))

    else: 
        print ("You have 1 seat left! ") 
    
    name = input("Name: ")
    count += 1
    print () 

    
if count == MAX_TICKETS:
    print ("You have sold all available tickets!")
else: 
    print ("You have sold {} tickets. \n" "There are {} places still available" .format(count, MAX_TICKETS - count))


