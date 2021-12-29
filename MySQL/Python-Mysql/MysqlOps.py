

"""	
@Author: Aishwarya
@Date: 2021-12-17
@Last MOdified:2021-12-19
@Title : Database
"""
########################################################################################################

import mysql.connector

class TestDB:

    def __init__(self):
     """"
    Description: It is counstructor .connecting  to Database
    Parameter: none
    Return: none
    """
    try:
        conn= mysql.connector.connect(host="localhost",user="root",passwd="Mysql@1234",database="MIS") 
        if conn.is_connected():
            print("Connection is successful")  
        else:
            print("Connection failed")  
    except Exception as e:
        print(e)
    print()
    def show_tables(self):
        """"
        Description: Displaying tables present in database
        Parameter: none
        Return: none
        """
        try:
            self.cursor = self.conn.cursor()
            ## executing the statement using "execute()" method
            print("Tables :")
            print()
            self.cursor.execute("SHOW TABLES")
            # it returns a list of all databases present
            self.tables = self.cursor.fetchall()
            #showing one by one database
            for table in self.tables:
                print(table)
        except Exception as e:
            print(e)
    def create_table(self):
        """"
        Description: creating table 
        Parameter: none
        Return: none
        """
        try:
            self.db = self.conn.cursor()
            self.db.execute("SHOW TABLES")
            print()       
            self.tables = self.db.fetchall() 
            for table in self.tables:
               print(table)
            print()
            ## creating a tables
            self.db.execute("CREATE TABLE customers (customerID INT,name VARCHAR(50),city VARCHAR(50),state VARCHAR(50),postalcode INT(7),country VARCHAR(50));")
            print("customers Table is created successfully")
            #describing table
            self.db.execute("DESC TABLE customers")
            print(self.db.fetchall())
        except Exception as e:
            print(e)


    def table_exist(self):
        """"
        Description: checking if table exist 
        Parameter: none
        Return: none
        """
        try:
            self.db = self.conn.cursor()
            self.db.execute("SHOW TABLES")
            print()       
            self.tables = self.db.fetchall() 
            for table in self.tables:
                print(table)
            print()
            table=input("Enter table name :")     
            if (table,) in self.tables:
                print()
                print("Table is exist")
            else:
                print("Table is not exist")
            
            self.db.execute("DESC TABLE customers")
            print(self.db.fetchall())
        except Exception as e:
            print(e)

    def drop_table(self):
        """"
        Description: dropping table from database
        Parameter: none
        Return: none
        """
        try:
            self.db = self.conn.cursor()
            self.db.execute("SHOW TABLES")
            ## drop a table 
            self.tables = self.db.fetchall() 
            for table in self.tables:
                print(table)
            print() 
            table=input("Enter table name to drop:")     
            if (table,) in self.tables:
                print()
                print("Table is exist")
                ans=input("Are you sure want to drop : please enter y or n :")
                if ans=="y":
                    self.db.execute("DROP TABLE {}".format(table))
                    print("Table dropped successfully")
                elif ans=="n":
                    print("table is not dropped")
            else:
                print("Table is not exist")
            print()
               
            
        except Exception as e:
            print(e)
   
    def insert_data(self):
        """"
        Description: inserting data into table
        Parameter: none
        Return: none
        """
        try:
            #self.table_exist()

            self.cursor = self.conn.cursor()
           
            ## defining the Query
            query = "INSERT INTO customers(customerID ,name,city,state,postalcode,country) VALUES (%s,%s,%s,%s,%s,%s)"
            ## storing values inn a variable
            values =[ (1,"John Doe", "New York","New York",5643,"USA"),(2,"Monica", "New York","New York",5643,"USA"),
            (3,"Jerry", "Manhattan","New York",6453,"USA"),(4,"Tom", "Boston","Texas",3666,"USA"),
            (5,"Matt", "LA","LA",7893,"USA")]
            #     ## executing the query with values
            self.cursor.executemany(query,values)
        
            self.conn.commit()

            print(self.cursor.rowcount, "record inserted")
        except Exception as e:
            print(e)

    def print_tabledata(self):
        """"
        Description: printing table content
        Parameter: none
        Return: none
        """
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute("SELECT * FROM customers")
            result = self.cursor.fetchall()
            for data in result:
                print(data)
            self.conn.commit()
        except Exception as e:
            print(e)

    def update_tabledata(self):
        """"
        Description: updating row content of table 
        Parameter: none
        Return: none
        """
        try:
            self.cursor = self.conn.cursor()
            query = "UPDATE customers SET city = 'Buffalo' WHERE customerID =2 "
            self.cursor.execute(query)
            self.conn.commit()
            print(self.cursor.rowcount, "record(s) affected") 
            self.print_tabledata()
        except Exception as e:
            print(e)

    def delete_tabledata(self): 
        """"
        Description: deleting row content of table 
        Parameter: none
        Return: none
        """

        try:
            self.cursor = self.conn.cursor()
            query = "DELETE FROM customers WHERE city = 'LA' "
            self.cursor.execute(query)
            self.conn.commit()
            print(self.cursor.rowcount, "record(s) affected") 
            self.print_tabledata()
        except Exception as e:
            print(e)

if __name__ == "__main__":

    try:  
        test=TestDB() 
        while(True):
            print("1.Create Table")
            print("2.Drop Table") 
            print("3.Insert data into Table")
            print("4.Print data of Table")
            print("5.Update data of Table")
            print("6.Delete data of Table")
            print("7.Exit")

            choice = int(input("Enter choice :"))            
            if choice == 1:
                test.create_table()
            elif choice == 2:
                test.drop_table()
            elif choice == 3:
                test.insert_data()
            elif choice==4:
                test.print_tabledata()
            elif choice==5:
                test.update_tabledata()
            elif choice==6:
                test.delete_tabledata()
            else:
                break
    except Exception as e:
        print(e)
  
    
    
    
    
