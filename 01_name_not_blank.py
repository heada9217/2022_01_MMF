
# function to check name is not blank

def not_blank(question, error_message):
    valid = False 

    while not valid: 
        response = input(question) 

        if response != "": 
            return response 
        else:
            print(error_message)



name = not_blank("What is your name?: ", "Sorry, please fill out a name before continuing.") 
