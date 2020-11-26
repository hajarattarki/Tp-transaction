import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-J5TPNKP;'
                      'Database=WideWorldImporters;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT CustomerID ,CustomerName FROM WideWorldImporters.Sales.Customers')

cursor.execute('''
                UPDATE WideWorldImporters.Sales.Customers
                SET CustomerID = Amel
                WHERE Name = '3'
                ''')

conn.commit()
for row in cursor:
    print(row)
