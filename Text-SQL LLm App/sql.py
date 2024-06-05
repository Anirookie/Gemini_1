import sqlite3

## Connect to sqlite
connection=sqlite3.connect("student.db")

## Create a cursor object to insert, record, create table, retrieve
cursor=connection.cursor()

## create the table

cursor.execute("""
        CREATE TABLE STUDENT(
        NAME VARCHAR(25),
        CLASS VARCHAR(25),
        SECTION VARCHAR(25),
        MARKS INT)
    """)

## Insert Some more records

cursor.execute('''Insert Into STUDENT values('Mira','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('Sudhanshu','Data Science','B',100)''')
cursor.execute('''Insert Into STUDENT values('Darius','Data Science','A',86)''')
cursor.execute('''Insert Into STUDENT values('Viks','DEVOPS','A',50)''')
cursor.execute('''Insert Into STUDENT values('Emirate','DEVOPS','A',35)''')

## Disspaly ALl the records

print("The inserted records are")
data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

## Commit your changes in the database
connection.commit()
connection.close()