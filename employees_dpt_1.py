import sql_connect as sqlcon

# Creating a function to import main.py and run main screen.  Function used to avoid circular import. 
def imp_main():
    import main as m
    m.choice_launch(m.main_options())


def emp_dpt():

    # Getting employee & department data from the SQL connect function. 
    emp_dpt = sqlcon.get_emp_dpt()

    # Indicies for looping. 
    lenght = len(emp_dpt)
    start = 0
    finish = 2
    
    while True:
        print ("\nEmployee\t\t|\t\t Department")
        print ("______________\t\t|\t\t ________________________")
        
        # Printing the employees as pairs, through the defined indices. 
        for i in emp_dpt[start:finish]:
            print (i["Employee"], "\t\t|\t\t", i["Department"])
        

        # Add two to each index to return the next two employees.
        start = start +2
        finish = finish +2

        # If our list of employees is an odd number, the final index will become out of range and the programme will throw an error. 
        # We can solve this before the out of range index goes through the for loop, by returning on the last entry. 
        if finish == lenght +1:
            start = -1
            finish = lenght

        # if the iteration is complete, return to main menu.
        if finish > lenght:
            imp_main()

        # Giving user the option to quit. 
        print ("-- Quit (q) --")
        user_input = input()
        
        # If user selects to quit, return to the main menu
        if user_input == "q":
            imp_main()