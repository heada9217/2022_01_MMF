
import string


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




def instructions(options):
    show_help = 'Invalid choice'
    show_error = 'Please answer with yes or no.'
    while show_help == 'Invalid choice':
        show_help = input("Would you like to read the instructions?")
        show_help = string_check(show_help, options, show_error)

    if show_help == 'yes':
        print()
        print("**** Mega Movie Fundraiser Instructions ****")
        print()
        print("")

    return ""

#Main Routine goes here

#list for valid yes / no responses
yes_no = [
    ["yes", "y"],
    ["no","n"]
]

#Ask if instructions are needed 
instructions(yes_no)
print()
print("Program Launching...")