import sql_connect as sqlcon
import employees_dpt_1 as ed


def emp_salary():
    
    # This will prompt the user to keep checking salaries until they pass in "q"
    while True:
        print("\nEnter (q) to Quit")
        choice = input("\nEnter EID: ")
        
        # If input is "q", return to main menu.
        if choice =="q":
            ed. imp_main()
        
        # Otherwise, get the salary data for EID. 
        else:
            salary = sqlcon.get_salary(choice)

            for i in salary:
                # If EID is in the database, return their salary. 
                if i["eid"] == choice.upper():  # Convert to upper as python is case sensitive (sql is not)
                    print ("\nSalary Details For Employee: {}\n--------------------------------".format(choice))
                    print ("Minimum", "\t|\t", "Average", "\t|\t", "Maximum")
                    print (i["Minimum"], "\t|\t", i["Average"], "\t|\t", i["Maximum"])
                
                
                # Otherwise, if the input EID is not in database, return blank salary data.
                else: 
                    print ("\nSalary Details For Employee: {}\n--------------------------------".format(choice))
                    print ("Minimum", "\t|\t", "Average", "\t|\t", "Maximum")

