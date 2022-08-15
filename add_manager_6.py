import sql_connect as sqlcon
import employees_dpt_1 as ed
import ne04j_connect as neo


def new_manager ():
    while True:
        # temp folders to append any edi/ did that exists in the database.  For checking if they exist. 
        temp_eid = []
        temp_did = []

        # eid is new_data[0] and did is new_data[1]
        new_data = []

        print("\nEnter (q) to Quit")
        
        # Requesting EID input. 
        new_data.append(input("\nEnter EID: ").upper())
        
        
        if new_data[0] == "Q":
            ed.imp_main()

        # Requesting DID input
        new_data.append(input("Enter DID: ").upper())

        # Getting the EIDs that exist in database. 
        all_eid = sqlcon.get_eid()

        # Getting the DIDs that exist in database. 
        all_did = sqlcon.get_did()

        # appending existing EIDs to eid temp folder.
        for i in all_eid:
            temp_eid.append(i["EID"])

        # appending existing DIDs to did temp folder.
        for i in all_did:
            temp_did.append(i["DID"])

        # If both eid and did exist in database, continue to assign new manager. 
        if new_data[0] in temp_eid and new_data[1] in temp_did:

            # Checking if department has a manager assigned on Neo4j. 
            relationship = neo.read_trans(neo.get_dpt_relationship, new_data[1])

            # If the lenght of relationship is 2, then did is already assigned to an employee. 
            if len(relationship) == 2:
                print ("\nDepartment {} is already managed by Employee {}".format(relationship[0], relationship[1]))
            
            # Otherwise no manager assigned, so proceed to assign the manager to the department. 
            else:
                neo.write_function(neo.new_manager,new_data)
                print("\nEmployee  {}  now manages Department  {}".format(new_data[0], new_data[1]))

        # if the inputted eid is not in the temp folder, notify the user and loop back around. 
        if new_data[0] not in temp_eid:
            print("\nEmployee {} does not exist".format(new_data[0]))

        # if the inputted eid is not in the temp folder, notify the user and loop back around. 
        if new_data[1] not in temp_did:
            print ("\nDepartment {} does not exist\n".format(new_data[1]))
        