## Employees_department program

<br>

A python program to manage employees and departments in an organisation.  The program will connect to a SQL database to get employee data (names, date of birth and salary) and department data (names, location, budgets) and connect to Neo4j database to get the names of the employee that manages each department.  

<br>

The program can perform 8 functions, including exiting the application. These functions are listed below. 

<br>


![main menu](https://raw.githubusercontent.com/RYANCOX00/Employees/main/images/main_menu.PNG)

***

<br>

## Steps to install

<br>

1. It is recommended that Windows users download Cmder to interact with the command line. Cmder can be downloaded [here](https://cmder.net/).   Mac and Linux user may continue to use the built in command line. 

2. To run this code a user will require Python 3 and the below listed packages to be installed.  It is recommended that a user downloads Anaconda as these particular packages are already pre-installed.  You can download Anaconda [here](https://www.anaconda.com/products/individual).  Alternatively, Python 3 can be downloaded [here](https://www.python.org/downloads/). 


3. In addition to anaconda the user will also need to install pymysql and neo4j libraries.  This is completed by typing the following code into the terminal

<br>

```
pip3 install pymysql
```
<br>

and

<br>

```
pip3 install neo4j
```


4. The user will require a SQL server. It is recommended that the user installs the mySQL which is available [here](https://www.mysql.com/downloads/)



5. The user will need to install the neo4j server. This is available [here](https://neo4j.com/download-neo4j-now/?utm_program=emea-prospecting&utm_source=google&utm_medium=cpc&utm_campaign=emea-search-offers&utm_adgroup=dynamic&utm_content=dynamic&utm_placement=&utm_network=g&gclid=Cj0KCQjw3eeXBhD7ARIsAHjssr_5lcHocfIZ4HCyQoBdDxMgDU2DfpcyyjnCtxUpqitZwAvjSqrj6IEaAnN8EALw_wcB).  This will also allow you to interact with the neo4j browser via the [localhost](http://localhost:7474/). 


6. Once a MySQL and Neo4j accounts are set up, the databases in the data folder should be imported. 

7. Users will be required to download Git in order to pull contents from the repository into a local directory. Git is available [here](https://git-scm.com/downloads). 

***

<br>

## Run

<br>

1. To pull the code to a local directory a user will first need to clone this repository using the SSH. Go to your desired directory in the command line and type 

```
gitclone git@github.com:RYANCOX00/Employees.git
```

2. In the command line or on a code edit terminal of your choice go to the local directory you pulled the code to and run the main.py file. 

```
python main.py
```

<br>

***

## Contact

<br>

Should any person wish to contact me in relation to the content of this workbook, they can contact me by email: [Ryan Cox](mailto:ryancox212@gmail.com?subject=[GitHub]%20Source%20Han%20Sans)

***
# End