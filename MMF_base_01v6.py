#import statements 
import re 
import pandas

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

#Checks number of tickets left and warns user 
#if maximum is being approached
def check_tickets(tickets_sold, ticket_limit):
    if tickets_sold < ticket_limit - 1:
        print("You have {} seats"  " left".format(ticket_limit - tickets_sold))

    #warns user that there is only 1 seat left
    else:
        print("There is only one seat left !")

    return ""

# gets ticket price based on age 
# age is checked with integer checker
def get_ticket_price():
     
     #get age between 12 and 130 
    age = int_check("Age: ")

    if age < 12:
        print("Sorry, you are too young for this")
        return ("Invalid ticket price")
    elif age > 130:
        print("That must be a mistake, that is too old !")
        return ("Invalid ticket price")

    if age < 16:
        ticket_price = 7.5 

    elif age < 65:
        ticket_price = 10.5

    else: 
        ticket_price = 6.5 
    
    return ticket_price

def string_check(choice, options, error):

    for var_list in options:

        #if the snack is in one of the lists, return the full
        if choice in var_list:

            #Get full name of snack and put it 
            #in title case so it looks nice when outputted
            chosen = var_list[0].title()
            is_valid = "yes"
            break

        #if choice is not valid, set is_valid to no 
        else:
            is_valid = "no"
            # print(error)
        
    #if the snack is not OK = ask question again 
    if is_valid == "yes":
        return chosen
    else:
        print(error)
        return "Invalid choice"

def get_snack():
    #checks whether the item starts with a number
    number_regex = "^[1-9]"


    #valid snacks holds list of all snacks 
    #Each item in val id snacks is a list with 
    #valid options for each snack [full name and letter code and abbreviations.]
    snack_error = "Please enter a valid snack"
    
    valid_snacks = [
    ["popcorn", "p", "corn", "a"],
    ["M&Ms", "M&M's", "m&m's", "mms", "mm", "b"],
    ["Pita Chips", "chips", "pc", "pita", "c"],
    ["water", "w", "d"],
    ["orange juice", "oj", "juice", "e"]
    ]
    #holds snack order for a single user. 
    snack_order = []

    desired_snack = ""
    while desired_snack != ("xxx"):

        snack_row = [] 

        #ask user for desired snack and put it in lowercase 
        desired_snack = input("Snack: ").lower()

        if desired_snack == "xxx":
            return snack_order

        #if item has a number, seperate it into two (number / item)
        if re.match(number_regex, desired_snack):
            amount = int(desired_snack[0])
            desired_snack = desired_snack[1:]

        else:
            amount  = 1 
            desired_snack = desired_snack

        #remove white space around snack 
        desired_snack = desired_snack.strip()

        #check if snack is valid
        snack_choice = string_check(desired_snack, valid_snacks, snack_error)

        #check snack amount is valid (less than 5)
        if amount >= 5:
            print("Sorry, you are only allowed a maximum of 4 of each snack")
            snack_choice = "Invalid choice"
        
        #add snack and amount to list 

        snack_row.append(amount)
        snack_row.append(snack_choice)

        #check that snack is not the exit code before adding 
        if snack_choice != "xxx" and snack_choice != "Invalid choice":
            snack_order.append(snack_row)
    
# ******* MAIN ROUTINE ***********

#Set up dictionaries / lists needed to hold data 

#list for valid yes / no responses
yes_no = [
    ["yes", "y"],
    ["no","n"]
]
        
yes_no_error = "Please answer with yes or no"        

#list of valid responses for payment method
pay_method = [
    ["cash", "ca"],
    ["credit", "cr"]
]

# Ask user if they have used the program before and show instructions if necessary

# Initialize loop so that is runs at least once 

MAX_TICKETS = 5
name = ""
ticket_count = 0 
ticket_sales = 0

#Initialise lists (to make data-fram in due course)
all_names = []
all_tickets = []

popcorn = []
mms = []
pita_chips = [] 
water = []
orange_juice = [] 

snack_lists = [popcorn, mms, pita_chips, water, orange_juice]

surcharge_mult_list = []


#Data Frame Dictionary 
movie_data_dict = {
    'Name': all_names,
    'Ticket': all_tickets,
    'Popcorn': popcorn,
    'Water': water,
    'Pita Chips' : pita_chips,
    'M&Ms': mms,
    'Orange Juice': orange_juice,
    'Surcharge Multiplier': surcharge_mult_list
    }

#cost of each snack
price_dict = {
    'Popcorn': 2.5,
    'Water' : 2,
    'Pita Chips': 4.5,
    'M&Ms': 3, 
    'Orange Juice': 3.25
    }



while name != "xxx" and ticket_count < MAX_TICKETS:

    #checks numbers of ticket limit has not been exceeded
    check_tickets(ticket_count,MAX_TICKETS)

    #Gets details of each ticket
    
    #Get name (Cant be blank)
    name = not_blank("What is your name?: ", "Sorry, please fill out a name before continuing.")
    
    if name == ("xxx") and ticket_count > 0:
        break 
    elif name == "xxx":
        name = ""
        print("You need to sell at least one ticket")
        continue



    #get ticket price based on age
    ticket_price = get_ticket_price()
    #If age is invalid, restart loop (and get name again)
    if ticket_price == "Invalid ticket price":
        continue 
    
    ticket_count += 1
    ticket_sales += ticket_price

    #Add name and ticket price to lists
    all_names.append(name)
    all_tickets.append(ticket_price)

    #gets snacks of each ticket
    #asks user if they want a snack 
    check_snack = "Invalid choice"
    while check_snack == "Invalid choice":  
        want_snack = input("Do you want to order snacks? ").lower()
        check_snack = string_check(want_snack, yes_no, yes_no_error)

     #if they say yes, ask what snacks they want and add to our order
    if check_snack == "Yes":
        snack_order = get_snack()

    else:
        snack_order = []

    #Assume no snacks have been bought....
    for item in snack_lists:
        item.append(0)

    for item in snack_order:
        if len(item) > 0:
            to_find = (item[1])
            amount = (item[0])
            add_list = movie_data_dict[to_find]
            add_list[-1] = amount

    # Calculate snack price 

    # ask for payment method (and apply surcharge if necessary)
    pay_error = "Please answer with cash or credit."
    
    #Ask for payment method
    how_pay = "Invalid choice"
    while how_pay == "Invalid choice":
        how_pay = input("Please choose a payment method, cash(ca) or credit (cr)").lower()
        how_pay = string_check(how_pay, pay_method,pay_error)
    
    if how_pay == "Credit":
        surcharge_mulitplier = 0.05 
    else: 
        surcharge_mulitplier = 0
    
    surcharge_mult_list.append(surcharge_mulitplier)


#End of tickets / snacks / payment 


#Create dataframe and set index to name column
movie_frame = pandas.DataFrame(movie_data_dict)
movie_frame = movie_frame.set_index('Name')

#create column called 'Sub Total'
#fill it price for snacks and ticket 

movie_frame['Snacks'] = \
    movie_frame['Popcorn']*price_dict['Popcorn'] + \
    movie_frame['Water']*price_dict['Water'] + \
    movie_frame['Pita Chips']*price_dict['Pita Chips'] + \
    movie_frame['M&Ms']*price_dict['M&Ms'] + \
    movie_frame['Orange Juice']*price_dict['Orange Juice']

movie_frame['Sub total'] = \
    movie_frame['Ticket'] + \
    movie_frame['Snacks']

movie_frame['Surcharge'] = \
    movie_frame['Sub Total'] * movie_frame['Surcharge Multiplier']

movie_frame["Total"] = movie_frame["Sub Total"] + \
    movie_frame["Surcharge"]


# movie_frame = pandas.DataFrame(movie_data_dict,
#                      columns=['Ticket', 'Name', 'Popcorn', 'Water', 'Pita Chips', 'M&Ms', 'Orange Juice', 'Sub Total'])

small_frame = movie_frame[['Sub Total', 'Ticket', 'Surcharge', 'Total']]

movie_frame = movie_frame.reindex(columns=['Ticket', 'Popcorn', 'Water', 'Pita Chips', 'M&Ms', 'Orange Juice', 'Sub Total'])


movie_frame = movie_frame.rename(columns={'Orange Juice': 'OJ', 'Pita Chips': 'Chips', 'Surcharge Multiplier' : 'SM'})

pandas.set_option('display.max_columns', None)

pandas.set_option('precision', 2)

print_all = input("Print all columns?? (y) for yes")
if print_all == "y":
    print(movie_frame)
else:
    print(small_frame)

print()

# Calculate Total sales and profit 

# Output data to test file 