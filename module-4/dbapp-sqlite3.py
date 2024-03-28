import sqlite3

# Database create and connect 

try:
    db_connect=sqlite3.connect("db_sqlite3")
    print("Database created/connected")
except Exception as a:
    print(a)

# table create
    
# table_create="create table student(id integer primary key autoincrement,firstname text,lastname text,sub text)"
# try:
#     db_connect.execute(table_create)
#     print("table created")
# except Exception as a:
#     print(a)

# insert data 

# insert_data="insert into student(firstname,lastname,sub)values('nirav','pansuriya','painting'),('dhruv','vadaliya','physics'),('navanit','pambhar','veterinary'),('piyush','vadaliya','farming')"
# try:
#     db_connect.execute(insert_data)
#     db_connect.commit()
#     print("data inserted")
# except Exception as a:
#     print(a)


# update data

# update_data="update student set sub='battery' where id=5"
# try:
#     db_connect.execute(update_data)
#     db_connect.commit()
#     print("record Updated")
# except Exception as a:
#     print(a)

# delete record

# delete_data="delete from student where id=5"
# try:
#     db_connect.execute(delete_data)
#     db_connect.commit()
#     print("record deleted")
# except Exception as a:
#     print(a)
    
# fetch data 
cr=db_connect.cursor()
fetch_data="select * from student"
try:
    cr.execute(fetch_data)
    # data=cr.fetchone()
    # data=cr.fetchmany(3)
    data=cr.fetchall()
    print(data)
except Exception as a:
    print(a)
