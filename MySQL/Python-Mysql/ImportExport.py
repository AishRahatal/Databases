
"""	
@Author: Aishwarya
@Date: 2021-12-17
@Last M0dified:2021-12-20
@Title :Write a Python program import and export mysql file
"""
########################################################################################################

import os
import mysql.connector


class ImportExport():
    '''
    Description : performing import and export of databases
    '''
    def __init__(self):
         """"
    Description: It is counstructor .creating connection Database
    Parameter: none
    Return: none
    """
    try:
        conn= mysql.connector.connect(host="localhost",user="root",passwd="Mysql@1234",database="sample") 
        if conn.is_connected():
            print("Connection is successful")  
        else:
            print("Connection failed")  
    except Exception as e:
        print(e)

    def export_db(self):
        '''
        Description : To export database(sample) to file (sampledb.sql)
        parameter : self
        ''' 
        try:
            os.system("mysqldump -u root -p sample > sampledb.sql")
            print("exported db")
        except Exception as e:
            print(e)

    def import_db(self):
        '''
        Description : To import file (test.sql) data into new database(test) 
        parameter : self
        ''' 
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute("CREATE DATABASE testDB")
            print("Database created")
            os.system("mysql -u root -p testDB < test.sql")
            self.cursor.execute("SHOW DATABASES")
            result = self.cursor.fetchall()
            for d in result:
                print(d)
        except Exception as e:
            print(e)

if __name__ == '__main__':
    obj = ImportExport()
    try:   
        while(True):
            print("1.Export database")
            print("2.Import database") 
            print("3.Exit")
            choice = int(input())            
            if choice == 1:
                obj.connection_establish()
            elif choice == 2:
                obj.export_db()
            elif choice == 3:
                obj.import_db()
            else:
                break
    except Exception as e:
        print(e)