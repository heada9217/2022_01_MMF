#valid snacks holds list of all snacks
#each item in valid snacks is a list with 
#valid options for each snack [full name, letter code, (a-e) and possible abbreviations ]
valid_snacks =[
    ["popcorn", "p", "corn", "a"],
    ["M&M's", "m&m's", "mms", "mm", "b"],
    ["pita_chips", "chips", "pc", "pita", "c"],
    ["water", "w", "d"],
    ["orange juice", "oj", "juice", "e"]
]

#initialize variables
snack_ok = ""
snack = ""

#loop for testing 
for item in range(0,100):


    #ask user for desired snack and put it in lowercase 
    desired_snack = input("Snack: ").lower()

    for var_list in valid_snacks:

        #if the snack is in one of the lists, return the full: :
        if desired_snack in var_list:

            #get full name of snack and put it 
            #in title case so it looks nice when outputted
            snack = var_list[0].title()
            snack_ok = "yes"
            break
        
        #if the chosen snack is not valid, set snack_ok to no
        else:
            snack_ok = "no"

    if snack_ok == "yes":
        print("Snack Choice: ", snack)
    else:
        print("Invalid choice")

        
