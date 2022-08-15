import sql_connect as sqlcon
import employees_dpt_1 as ed

# A function to call the sql query and save result as a variable. 
def first_time(dept):
    dept = sqlcon.get_all_dpt()
    print("connected")
    return dept


# A function to print the results saved under the dept variable. 
def dept_full_details (dept):
    
    # Printing column headings. 
    print ("\nDid \t\t| Name \t\t\t\t| Location \t| Budget")
    
    # printing the data.  There is different tabs depending on the len of data in Name column (to straighten columns)
    for i in dept:
        if len(i["Name"]) < 22 and len(i["Name"]) >=13 :
            print (i["Did"], "\t\t|", i["Name"], "\t\t|", i["Location"], "\t\t|", i["Budget"])
    
    
        elif len(i["Name"]) < 13:  
            print (i["Did"], "\t\t|", i["Name"], "\t\t\t|", i["Location"], "\t\t|", i["Budget"])
        else:
            print (i["Did"], "\t\t|", i["Name"], "\t|", i["Location"], "\t\t|", i["Budget"])
    
    # Press q to quit.
    while True:
        quit = input("Enter (q) to return to main screen: ")
        
        if quit == "q":
            ed.imp_main()