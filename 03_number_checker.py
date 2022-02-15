#function to check the age

def int_check(question, low_num, high_num):

    error = "Please enter a whole number between {} and {}".format(low_num, high_num)
    
    valid = False 
    while not valid:

        try:
            response = int(input(question)) 
            
            if low_num <= response <= high_num:
                return response
            
            else:
                print (error)
        
        except ValueError:
            print(error)
    
age = int_check("Age: ", 12, 130)