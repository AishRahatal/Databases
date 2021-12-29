'''	
@Author: Aishwarya
@Date: 2021-12-22 
@Last Modified: 2021-12-23
@Title : Importing file to databases
'''
#########################################################################################

import json
import pandas as pd
from pymongo import MongoClient
from bson.json_util import dumps, loads

# Making Connection
myclient = MongoClient("mongodb://localhost:27017/")

# database
db = myclient["filesdb"]

# Created or Switched to collection for json
Collection = db["jsondata"]
#created another collection for csv
col=db["csvdata"]
def import_json():
    # Loading or Opening the json file
    with open('import_data.json') as file:
        file_data = json.load(file)
        
    # Inserting the loaded data in the Collection
    # if JSON contains data more than one entry
    # insert_many is used else inser_one is used
    if isinstance(file_data, list):
        Collection.insert_many(file_data)
    else:
        Collection.insert_one(file_data)

    print()
    print("Data in Json file")
    print("------------------------")
    print(file_data)
    print()
    
def import_csv():
    try:
        with open('Import_emp.csv', 'r') as read_obj:
            # pass the file object to reader() to get the reader object
            data= pd.read_csv(read_obj)
            data_json = json.loads(data.to_json(orient='records'))
            if isinstance(data_json, list):
                col.insert_many(data_json)
            else:
                col.insert_one(data_json)        #print list of inserted documents:
            print()
            print("Data in CSV file")
            print("------------------------")
            print(data_json)
            print()
    except Exception as e :
        print(e)
def exportdata_json():
    try:
        # Connecting to the database named
        mydatabase = db.filesdb

        # Accessing the collection named
        # gfg_collection
        mycollection = mydatabase.csvdata

        # Now creating a Cursor instance
        # using find() function
        cursor = mycollection.find()

        # Converting cursor to the list
        # of dictionaries
        list_cur = list(cursor)

        # Converting to the JSON
        json_data = dumps(list_cur, indent = 2)

        # Writing data to file data.json
        with open('export_empdata.json', 'w') as file:
            file.write(json_data)
    except Exception as e :
        print(e)


if __name__=='__main__':
    #import_json()
    #import_csv()
    exportdata_json()