name = "",not_blank("Name:", "Please fill out a name before continuing")
count = 0 
MAX_TICKETS = 5 

while name != "xxx" and count <MAX_TICKETS:


    name = input("Name: ")
    count += 1
    print () 
    
if count == MAX_TICKETS:
    print ("You have sold all available tickets!")
else: print ("You have sold () tickets. \n" "There are () places still available" .format(count, MAX_TICKETS - count))

if count == 4: 
    print ("1 ticket left!")

def not_blank(question, error_question):
    valid = False 

    while not valid:
        response = input(question)  

        if response != "":
            return response 
        else:
            print(error_question)
