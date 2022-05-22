# This is a sample Python script.
import pyodbc
import generator


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    for x in range(1, 50):
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=DESKTOP-7S9CDR1\SQLEXPRESS;'
                              'Database=database_name;'
                              'Trusted_Connection=yes;')
        conn.cursor()

        generator.generateSprzet()
        row = conn.fetchone()
        while row:
            print(row[0])
            row = conn.fetchone()