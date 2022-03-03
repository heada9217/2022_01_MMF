import re

# checks valid inpput based on a list of options, 
# includes a custom error message
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


#gets list of snacks 
def get_snack():
    #checks whether the item starts with a number
    number_regex = "^[1-9]"


    #valid snacks holds list of all snacks 
    #Each item in val id snacks is a list with 
    #valid options for each snack [full name and letter code and abbreviations.]
    snack_error = "Please enter a valid snack"
    
    valid_snacks = [
    ["popcorn", "p", "corn", "a"],
    ["M&M's", "m&m's", "mms", "mm", "b"],
    ["pita_chips", "chips", "pc", "pita", "c"],
    ["water", "w", "d"],
    ["orange juice", "oj", "juice", "e"]
    ]
    #holds snack order for a single user. 
    snack_order = []

    desired_snack = ""
    while desired_snack != "xxx":

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
            amount - 1 
            desired_snack = desired_snack

        #remove white space around snack 
        desired_snack = desired_snack.strip()

        #check if snack is valid
        snack_choice = string_check(desired_snack, valid_snacks, snack_error)

        #check snack amount is valid (less than 5)
        if amount >= 5:
            print("Sorry, you are only allowed 4 maximum of each snack")
            snack_choice = "Invalid choice"
        
        #add snack and amount to list 

        snack_row.append(amount)
        snack_row.append(snack_choice)

        #check that snack is not the exit code before adding 
        if snack_choice != "xxx" and snack_choice != "Invalid choice":
            snack_order.append(snack_row)

#Main Routine :

#valid option for yes / no 
yes_no_error = "Please answer with yes or no"
yes_no = [
    ["yes", "y"],
    ["no", "n"]
]

#asks user if they want a snack 
check_snack = "Invalid choice"
while check_snack == "Invalid choice":
    want_snack = input("Do you want to order snacks? ").lower()
    check_snack = string_check(want_snack, yes_no, yes_no_error)

#if they say yes, ask what snacks they want and add to our order
if check_snack == "Yes":
    get_order = get_snack(1)

else:
    get_order = []

#Show snack orders
print ()
if len(get_order) == 0:
    print("Snacks ordered: None")

else:
    print("Snacks Ordered: ")

    for item in snack_order:
        print(item)


    
    

