from neo4j import GraphDatabase

neo4jDriver = None

def neo_connect():
    url = "neo4j://localhost:7687"

    global neo4jDriver 
    neo4jDriver = GraphDatabase.driver(url, auth=("neo4j", "neo4j"))

# a function to get the did of each managed department. 
def get_managers (tx, module):
    query = "MATCH (e:Employee{eid: $name}) -[]-(d) return d.did"
    results = tx.run(query, name = module)

    names = []

    for result in results:
        names.append(result['d.did'])

    return names


# a function to read any query from a database, query based on the function provided as a parameter. 
def read_trans(function,query):
    neo_connect()
    with neo4jDriver.session() as session:
        results = session.read_transaction(function,query)
        return results


# A specific function to be provided into a read function to get data from a database.  Speficially did and eid of departments managed by employees. 
def get_dpt_relationship (tx, module):
    query = "MATCH (d:Department{did:$did}) <-[:MANAGES]-(e:Employee) RETURN d.did, e.eid"
    results = tx.run(query, did = module)

    names = []

    for i in results:
        names.append(i["d.did"])
        names.append(i["e.eid"])

    return names

# A function that will write to a database once a function and parameter is given. 
def write_function (function, query):
    neo_connect()
    with neo4jDriver.session() as session:
        session.write_transaction(function, query)


# A function that creates new node and/ or creates a relationship. Passed into write_function. 
def new_manager(tx,new_data):
    query = "MERGE (e:Employee{eid:$eid}) -[r:MANAGES]->(d:Department{did:$did}) RETURN e,r,d"
    tx.run(query,eid=new_data[0],did=new_data[1])