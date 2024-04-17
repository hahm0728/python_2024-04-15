import sqlite3

con=sqlite3.connect("c:\\work\\Employee.db")
cur=con.cursor()

cur.execute("select * from Employee;")
for row in cur:
    print(row)



