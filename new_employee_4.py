import sql_connect as sqlcon
import pymysql


# A function to read in attribute for the employee table. 
def new_details():
    eid = input("\nEID : ")
    name = input("Name : ")
    dob = input("DOB : ")
    dept = input("Dept ID : ")
    return eid, name, dob, dept

# A function to parse the attributes to the sql connection function. 
# Errors on the attributes conditions are handled here. 
def add_new(eid, name, dob, dept):
        try:
            sqlcon.insert(eid, name, dob, dept)
            print ("\nNew employee added.")
        
        # Errors are handled by code so they're specific. 
        except pymysql.err.IntegrityError as e:
            if e.args[0] == 1062:
                print("\n***Error ***: {} already exists".format(eid))
            
            elif e.args[0] == 1452:
                print("\n***Error***: Department {} does not exist".format(dept))
        
        except pymysql.err.OperationalError as e:
            if e.args[0] == 1292:
                print("\n***Error***: Invalid DOB: {}".format(dob))