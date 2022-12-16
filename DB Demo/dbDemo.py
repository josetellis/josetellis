import sqlite3
connect=sqlite3.connect("c://sqlite//hcl.db") # connection Object for Connecting Database
cur = connect.cursor() # Cursor Object To execute queries
# conn.execute('''CREATE TABLE Log(ID INT PRIMARY KEY     NOT NULL);''')
# print("Table created")
# conn.execute('''Insert into  Log  values(10);''')

# sql="""insert into filelog values(?,?);"""
# data=(100,'d://jose1//demo.txt')
# cur.execute(sql,data)
# connect.commit()
cur.execute("Select * from filelog where id=100");
rows=cur.fetchall()
for r in rows:
    print(r)
