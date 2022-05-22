# This is a sample Python script.
import pyodbc
import generator


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=DESKTOP-7S9CDR1\SQLEXPRESS;'
                          'Database=database_name;'
                          'Trusted_Connection=yes;')
    conn.cursor()

    for x in range(1, 50):

        generator.generateSprzet()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import pymssql
    conn = pymssql.connect(server='yourserver.database.windows.net', user='yourusername@yourserver', password='yourpassword', database='AdventureWorks')
    cursor = conn.cursor()
    cursor.execute("INSERT SalesLT.Product (Name, ProductNumber, StandardCost, ListPrice, SellStartDate) OUTPUT INSERTED.ProductID VALUES ('SQL Server Express', 'SQLEXPRESS', 0, 0, CURRENT_TIMESTAMP)")
    row = cursor.fetchone()
    while row:
        print "Inserted Product ID : " +str(row[0])
        row = cursor.fetchone()
    conn.commit()
    conn.close()