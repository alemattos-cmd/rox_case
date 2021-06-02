## created by Alessandro de Mattos Silva
## 02/06/2021
## alemattos-cmd

import pyodbc
server = '<server>.database.windows.net'
database = '<rox_bike>'
username = '<admin>'
password = '<admin>'   
driver= '{ODBC Driver 17 for SQL Server}'

with pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
    with conn.cursor() as cursor:
        cursor.execute("SELECT TOP 3 name, collation_name FROM sys.databases")
        row = cursor.fetchone()
        while row:
            print (str(row[0]) + " " + str(row[1]))
            row = cursor.fetchone()
            
