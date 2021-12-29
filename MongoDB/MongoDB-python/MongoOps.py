'''	
@Author: Aishwarya
@Date: 2021-12-22 
@Last Modified: 2021-12-23
@Title : python-MongoDB connection and CURD operations on mongo using python
'''
#########################################################################################

import pymongo

conn = pymongo.MongoClient("mongodb://127.0.0.1:27017/")

db=conn["demo"]
col=db["customers"]

def show_databases():
    """"
    Description: method to display databases present
    Parameter: none
    Return: none
    """
    try:
        if conn:
            print("Connection to database is successful")
            print("------------------------------------")
            databases = conn.list_database_names()
            #print(conn.list_database_names())
            print("List of Database :")
            print("------------------")
            for database in databases:
                print(database)   
            print()
        else: 
            print("Connection to database is failed")
        print("------------------------------------")

    except Exception as e:
        print(e)  

def exist_database():
    """"
    Description: method to check if database exist
    Parameter: none
    Return: none
    """
    try:
        print()
        dblist = conn.list_database_names()
        if "demo" in dblist:
            print("'demo' database exists.")
        else:
            print("'demo' databases is not exists.")
        print("------------------------------------")
    except Exception as e:
        print(e)  
def collections():
    """"
    Description: method to check if collection exist
    Parameter: none
    Return: none
    """
    try:
    
        print()
        collections_list = db.list_collection_names()
        print("Collections present in 'demo'database :")
        for c in collections_list:
            print(c)
        print("----------------------------------------")
        print()
        if "customers" in collections_list:
            print("'customers' collections exists.")
        else:
            print("'customers' collecton  is not exists.")
        print("------------------------------------")

    except Exception as e:
        print(e) 
def insert_documents():
    """"
    Description: method to insert into collection exist
    Parameter: none
    Return: none
    """
    try:
      
        mydict = { "name": "John", "address": "Highway 37" }

        x=col.insert_one(mydict)
        print("Inserting only one document:")
        print()
        print("current document id: ",x.inserted_id) 
        print()
        print("present document in customer collection :\n")
        print(mydict)
        print()
        print("----------------------------------------------------------")
        print("Inserting multiple documents")
        data =[
                { "name": "Amy", "address": "Apple st 652"},
                { "name": "Hannah", "address": "Mountain 21"},
                { "name": "Michael", "address": "Valley 345"},
                { "name": "Sandy", "address": "Ocean blvd 2"},
                { "name": "Betty", "address": "Green Grass 1"},
                { "name": "Richard", "address": "Sky st 331"},
                { "name": "Susan", "address": "One way 98"},
                { "name": "Vicky", "address": "Yellow Garden 2"},
                { "name": "Ben", "address": "Park Lane 38"},
                { "name": "William", "address": "Central st 954"},
                { "name": "Chuck", "address": "Main Road 989"},
                { "name": "Viola", "address": "Sideway 1633"}
                ]

        data_ids= col.insert_many(data)

        #print list of the _id values of the inserted documents:
        print("Id's of inserted data") 
        for i in data_ids.inserted_ids:
            print(i)
        print()
        print("-------------------------------------------")
        print("present documents in customer collection :\n")
        for d in data:
            print(d)
        print()
        print("------------------------------------------------------------------")

    except Exception as e:
        print(e)   

def find_docs():
    """"
    Description: method to display fields documents present in collection
    Parameter: none
    Return: none
    """
    try:
        print()
        print("Print data of fields of name and address of customer collection :")
        print("---------------------------------------------------------------------")
        for x in col.find({},{ "_id": 0, "name": 1, "address": 1 }):
            print(x)  
        print("-------------------------------------------")
        print()
    except Exception as e:
        print(e)   

def update_doc():
    """"
    Description: method to update  documents data present in collection
    Parameter: none
    Return: none
    """
    try:
        myquery = { "address": "Valley 345" }
        print("Before update :")
        print("----------------------------")
        old=col.find_one(myquery)
        print(old)
        print()
        print("---------------------------------")    
       
        newvalues = { "$set": { "address": "Canyon 123" } }

        col.update_one(myquery, newvalues)
        new={ "address": "Canyon 123" }
        #print "customers" after the update:
        print("After update :")
        print("----------------------------")
        new=col.find_one(new)
        print(new) 
        print()
        print("Updated successfully")
        print("----------------------------------")
    except Exception as e:
        print(e)   

def delete_doc():
    """"
    Description: method to delete documents data present in collection
    Parameter: none
    Return: none
    """
    try:
        myquery = { "address": "Mountain 21" }

        print("Before Delete :")
        print("----------------------------")
        del_query=col.find_one(myquery)
        print(del_query)
        print()
        print("---------------------------------")    

        col.delete_one(myquery) 
        
        #print "customers" after the update:
        print("After Delete :")
        for x in col.find():
            print(x) 
        print()
        print("Deleted successfully")
        print("----------------------------")
      
    except Exception as e:
        print(e)   

        

if __name__=='__main__':
    try:
        ch=None
        while ch!=0:
            #Choices
            print("----------------------------------------------------")
            print("Operations on mongoDB:")
            print(  "1:Show databases")
            print(  "2: Check 'demo' database is exists ")
            print(  "3: Check 'customer' collection exists in 'demo' database")
            print(  "4: Insert documents 'customer' to collection")
            print(  "5: Find documents in 'customer' collection")
            print(  "6: Update documents of 'customer' collection")
            print(  "7: Delete documents of 'customer' collection")
            print("0: Exit")
            print("-------------------")
            ch=int(input("Enter Choice:"))
            if ch==1:
                show_databases()

            elif ch==2:
                exist_database()
            elif ch==3:
                collections()
            elif ch==4:
                insert_documents()
            elif ch==5:
                find_docs()
            elif ch==6:
                update_doc()
            elif ch==7:
                delete_doc()
            else:print("Exit")
    except Exception as e:
        print(e)         
    