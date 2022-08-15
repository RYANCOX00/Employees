import pymysql

# Defining connection 'conn' variable. 
conn = None

def connect_emp ():
    # function to connect to the employees database. 
    global conn 
    conn = pymysql.connect(host="localhost", user="root", password="root", db="employees", cursorclass=pymysql.cursors.DictCursor)
    


# A function to get employee names and department names from the employees database. 
def get_emp_dpt():
    connect_emp()

    # Query to get the employee name and department name.  
    query = """
    SELECT e.name as 'Employee', d.name as 'Department' 
    FROM employee e 
    inner join dept d 
    on e.did = d.did 
    ORDER BY Department, Employee;"""

    # Fetching the query data from the database.
    with conn:
        cursor = conn.cursor()
        cursor.execute(query)
        emp_dpt = cursor.fetchall()
      
        return emp_dpt


def get_salary(eid):
    connect_emp()

    # Query to get the EID, min, average and maxium salary.  
    query = """
    SELECT eid, FORMAT(min(salary),2) as Minimum, FORMAT(avg(salary),2) as Average, FORMAT(max(salary),2) as Maximum
    FROM salary
    WHERE eid = (%s);"""

    # Fetching the query data from the database.
    with conn:
        cursor = conn.cursor()
        cursor.execute(query, eid)
        salary = cursor.fetchall()
    
        return salary


def get_month(month):
    connect_emp()

    # Query to get the EID, name and DOB for a specific employee.  
    query = """
    SELECT eid as EID, Name, dob as 'Date of Birth'
    FROM employee
    WHERE (%s) = MONTH(dob);"""

    # Fetching the query data from the database.
    with conn:
        cursor = conn.cursor()
        cursor.execute(query, month)
        employee = cursor.fetchall()
    
        return employee


def insert(eid, name, dob, dept):
    connect_emp()

    ins = "INSERT INTO employee (eid, name, dob, did) VALUES (%s,%s,%s,%s);"


    with conn:
        cursor = conn.cursor()
        cursor.execute(ins, (eid, name, dob, dept))
        conn.commit()
    

def did_budget(list):
    connect_emp()

    query = "SELECT did AS Department, FORMAT(budget,0) as Budget FROM dept WHERE did IN %s;"

    
    with conn:
        cursor = conn.cursor()
        cursor.execute(query, [list])
        depart = cursor.fetchall()
    
        return depart

def get_eid():
    connect_emp()

    # Query to get the employee name and department name.  
    query = """
    SELECT eid as 'EID' 
    FROM employee;"""

    # Fetching the query data from the database.
    with conn:
        cursor = conn.cursor()
        cursor.execute(query)
        eid_dpt = cursor.fetchall()
      
        return eid_dpt

def get_did():
    connect_emp()

    # Query to get the employee name and department name.  
    query = """
    SELECT did as 'DID' 
    FROM Dept;"""

    # Fetching the query data from the database.
    with conn:
        cursor = conn.cursor()
        cursor.execute(query)
        did = cursor.fetchall()
      
        return did


def get_all_dpt():
    connect_emp()

    query = "SELECT did as Did, name as Name, lid as Location, budget as Budget FROM dept;"

    with conn:
        cursor = conn.cursor()
        cursor.execute(query)
        dept = cursor.fetchall()

        return dept
