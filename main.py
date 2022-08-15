# Employees programme
# Main Screen. Run this file to launch the programme. 

# Importing functions to launch tasks.
import employees_dpt_1 as ed
import view_salary_2 as vs
import month_search_3 as ms
import new_employee_4 as ne
import managed_dpt_5 as md
import add_manager_6 as am
import dept_details_7 as dd

# Assigning None to global variable. 
dept = None

# Function to request the users selection.
def main_options():
    
    print ("\nEmployees\n-------------")
    print("MENU \n----")
    print("1 - View Employees & Departments")
    print("2 - View Salary Details")
    print("3 - View by Month of Birth")
    print("4 - Add new Employee")
    print("5 - View Department managed by Employee")
    print("6 - Add Manager to Department")
    print("7 - View Department")
    print("x - Exit Application") 

# Requesting an input from the user. 
    while True:
        choice = (input("Choice: "))
        # User is forced to make a valid selection and choice is returned out of the function. 
        if choice in ["1", "2","3","4","5","6","7", "x"]:
            return choice
        
        # If not in list of choices the they will be asked to input again. 
        else:
            print("Enter a valid option.")

# A function to run the specified task. 
def choice_launch(choice):

    # View Employees
    if choice == "1":
        ed.emp_dpt()

    # View Salary
    elif choice == "2":
        vs.emp_salary()

    # View by Month of Birth
    elif choice == "3":
        ms.emp_dob()

    # Add new Employee
    elif choice == "4":
        # attributes read in from the user are put into a temp folder before being indexed into the function.  
        temp = []
        for i in ne.new_details():
            temp.append(i)
        
        ne.add_new(temp[0], temp[1], temp[2], temp[3])

    # View Department managed by Employee
    elif choice == "5":
        md.depart_manager()

    # Add new manager to department
    elif choice == "6":
        am.new_manager ()

    # If user chooses to view all departments
    elif choice == "7":
        
        # Using global variable for dept that is initially set to None. 
        global dept

        # If still None, run the query to call the SQL database. 
        if dept == None:
            try:
                dept = dd.first_time(dept)
                return dept

            # and continue by calling the function to print the contents of dept
            finally:
                dd.dept_full_details(dept)
        
        # If dept is no longer None, i.e. SQL query ran before, call the function to print the contents of dept
        else:
            dd.dept_full_details(dept)
        

    # x to close the application. 
    elif choice == "x":
       print ("Application closed")
       quit()

# Calling the function to start the programme. 
choice_launch(main_options())