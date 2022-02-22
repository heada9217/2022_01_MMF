#function to check the age

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

valid_age = 0
while valid_age == 0:
    age = int_check("Age: ")

    if age < 12:
        print("Sorry, you are too young for this")
        continue
    elif age > 130:
        print("That must be a mistake, that is too old !")
        continue
    else:
        break