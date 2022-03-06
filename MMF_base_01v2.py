#import statements 


#functions go here 

# checks that ticket name is not blank 
def not_blank(question, error_message):
    
    valid = False 

    while not valid: 
        response = input(question) 
        
        # If name is not blank, program continues
        if response != "": 
            return response 

        #if name is blank. show error (and repeat loop)
        else:
            print(error_message)

#checking for an interger between two values 
def int_check(question):

    error = "Please enter a whole number more than 0"
    
    valid = False 
    while not valid:

        try:
            response = int(input(question)) 
            
            if response <= 0:
                print(error)
            else:
                return response
        
        except ValueError:
            print(error)

#         MAIN ROUTINE

#Set up dictionaries / lists needed to hold data 

# Ask user if they have used the program before and show instructions if necessary

# Loop to get ticket details
 
MAX_TICKETS = 5
name = ""
ticket_count = 0 
ticket_sales = 0
 

while name != "xxx" and ticket_count < MAX_TICKETS:


    
    #Get name (Cant be blank)
    name = not_blank("What is your name?: ", "Sorry, please fill out a name before continuing.")
    
    if name == ("xxx") and ticket_count >0:
        break 
    elif name == "xxx":
        name = ""
        print("You need to sell at least one ticket")
        continue

    
    age = int_check("Age: ")

    if age < 12:
        print("Sorry, you are too young for this")
        continue
    elif age > 130:
        print("That must be a mistake, that is too old !")
        continue

    if age < 16:
        ticket_price = 7.5 

    elif age < 65:
        ticket_price = 10.5

    else: 
        ticket_price = 6.5 
    
    ticket_count += 1
    ticket_sales += ticket_price

    # tell user how many seats left
    if ticket_count < MAX_TICKETS - 1:
        print ("You have {} seats "
               "left ".format(MAX_TICKETS - ticket_count))

    else: 
        print ("You have 1 seat left! ") 

#End of tickets loop
#Calculate ticket profit...
ticket_profit = ticket_sales - (5 * ticket_count)
print("Ticket profit: ${:.2f}".format(ticket_profit))

    
if ticket_count == MAX_TICKETS :
    print ("You have sold all available tickets!")
elif ticket_count > 1:
    print ("You have sold {} tickets. \n" "There were {} tickets still available" .format(ticket_count, MAX_TICKETS - ticket_count))
else:
    print ("You have sold {} ticket. \n " "There were 4 tickets still available".format(ticket_count))



  

    

    # Get age (between 12 and 130)

    # Calculate ticket price 

    # Loop to ask for snacks 

    # Calculate snack price 

    # ask for payment method (and apply surcharge if necessary)


# Calculate Total sales and profit 

# Output data to test file 