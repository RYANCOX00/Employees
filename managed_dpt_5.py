import ne04j_connect as neo
import sql_connect as sqlcon
import pymysql
import employees_dpt_1 as ed


def eid_Input():
    eid = input("Enter EID: ")
    return eid.upper()



def depart_manager():


    while True:
        print ("\nEnter (q) to Quit\n")

        eid = eid_Input()

        if eid == "Q":
            ed. imp_main()
        
        else:
            try:
                departments = neo.read_trans(neo.get_managers, eid)
                depart = sqlcon.did_budget(departments)


                print ("\n Departments managed by: {}".format(eid))
                print ("___________________________________________")
                print ("\nDepartment\t| Budget")

                for i in depart:
                    print (i["Department"], "\t\t|", i["Budget"])

            except pymysql.Error as e:

                print ("\n Departments managed by: {}".format(eid))
                print ("___________________________________________")
                print ("\nDepartment\t| Budget")