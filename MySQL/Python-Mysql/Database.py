

'''	
@Author: Aishwarya
@Date: 2021-12-17
@Last MOdified:2021-12-18
@Title : Database
'''
########################################################################################################

import mysql.connector

class TestDB:

    def __init__(self):
     """"
    Description: It is counstructor 
    Parameter: none
    Return: none
    """
    try:
        db= mysql.connector.connect(host="localhost",user="root",passwd="Mysql@1234") 
        if db.is_connected():
            print("Connection is successful to MYSQL")  
        else:
            print("Connection failed")  
    except Exception as e:
        print(e)
    print()
    def show_databases(self):
        """"
        Description: creating connection
        Parameter: none
        Return: none
        """
        try:
            self.cursor = self.db.cursor()
            ## executing the statement using 'execute()' method
            print("Databases :")
            print()
            self.cursor.execute("SHOW DATABASES")
            # it returns a list of all databases present
            self.databases = self.cursor.fetchall()
            #showing one by one database
            for (database,) in self.databases:
                print(database)
        except Exception as e:
            print(e)

    def create_database(self):
        """"
        Description: accepting input from  user and storing into dictionary
        Parameter: none
        Return: none
        """
        try:
            self.cursor = self.db.cursor()
            self.cursor.execute("SHOW DATABASES")
            ## creating a databse called 'sample'
            self.databases = self.cursor.fetchall() 
            print() 
            database=input("Enter Database name :")     
            if (database,)in self.databases:
                print()
                print("Database is already present")  
            else:
                self.cursor.execute("CREATE DATABASE {}".format(database))
                print("Database is created")      
        except Exception as e:
            print(e)

    def drop_database(self):
        """"
        Description: accepting input from  user and storing into dictionary
        Parameter: none
        Return: none
        """
        try:
            cursor = self.db.cursor()
            ## creating a databse called 'sample'
            self.databases = self.cursor.fetchall() 
            print() 
            database=input("Enter Database name to drop:")     
            
            print()
            cursor.execute("DROP DATABASE {}".format(database))
            print("Database dropped successfully")
            
        except Exception as e:
            print(e)

    def connect_database(self):
        """"
        Description: accepting input from  user and storing into dictionary
        Parameter: none
        Return: none
        """
        try:
            self.condb= mysql.connector.connect(host="localhost",user="root",passwd="Mysql@1234",database="sample") 
            if self.condb:
                print("Connection is successful to Sample database")  
                
            else:
                print("Connection failed")  
               
        except Exception as e:
            print(e)
    def create_table(self):
        """"
        Description: accepting input from  user and storing into dictionary
        Parameter: none
        Return: none
        """
        try:
            cursor = self.condb.cursor()
            ## creating a tables 
            self.tables = self.cursor.fetchall() 
            print() 
            self.table=input("Enter table name :")     
            if self.table in self.tables:
                print()
                print("Table is already present")  
            else:
                cursor.execute("CREATE TABLE {}".format(self.table))
                print("Table is created")  
            cursor.execute("DESC TABLE {}".format(self.table))
        except Exception as e:
            print(e)
if __name__ == "__main__":
    test=TestDB()
    test.show_databases()
    test.create_database()
    #test.drop_database()
   