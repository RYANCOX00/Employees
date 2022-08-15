import sql_connect as sqlcon
import employees_dpt_1 as ed
from datetime import datetime

# A function to request a month input from the user. 
def emp_dob():

    # Until either try conditions are satisfied, request a valid month from the user. 
    print ("\nEnter (q) to Quit")
    while True:
        month_choice = input("Enter Month: ").capitalize()

        if month_choice =="Q":
            ed. imp_main()
        
        else:
            # If the input can be converted to an int, parse into function to read in data from sql. 
            try:
                month_choice = int(month_choice)
                if month_choice in [1,2,3,4,5,6,7,8,9,10,11,12]:
                    return print_details(month_choice)

            except:
                pass
            
            # If the month as string can be converted to a number i.e. Apr -> 4, parse into function to read in data from sql. 
            try:
                datetime_object = datetime.strptime(month_choice, "%b")
                month_choice = datetime_object.month
                return print_details(month_choice)

            except:
                pass


# A function to read employee data from sql database, using month to search. 
def print_details(month):
    emp_details = sqlcon.get_month(month)


    print ("EID\t| Name\t\t\t|Date of Birth")
    print ("______\t| _____________\t\t| ____________")

    for i in emp_details:
        print (i["EID"], "\t|", i["Name"], "\t\t|", i["Date of Birth"])

