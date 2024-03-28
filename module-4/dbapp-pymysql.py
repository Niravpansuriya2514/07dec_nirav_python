import pymysql

# database connect

try:
    db_conector=pymysql.connect(host='localhost',user='root',password='',database='hellodb')
    print("database connected")
except Exception as a:
    print(a)


cr=db_conector.cursor()

# Create Table

# create_table="create table freiend(id integer primary key auto_increment,name text not null,sub text,city text not null)"
# try:
#     cr.execute(create_table)
#     print("table created")
# except Exception as a:
#     print(a)

# Insert Data

# insert_data="insert into freiend(name,sub,city)values('nirav','marathon','junagadh'),('dhruv','physic','kachchh'),('nilesh','architecture','ahmedabad'),('bhavy','MBBS','junagadh'),('jash','IT','australia'),('dolar','automobile','dhari')"
# try:
#     cr.execute(insert_data)
#     db_conector.commit()
#     print("Data Inserted")
# except Exception as a:
#     print(a)

# Update Record

# updata_data="update freiend set city='rajkot' where name='nirav'"
# try:
#     cr.execute(updata_data)
#     db_conector.commit()
#     print("Record Updated")
# except Exception as a:
#     print(a)

# deleted table

# drop_table="drop table friend"
# try:
#     cr.execute(drop_table)
#     db_conector.commit()
#     print("Table Deleted ")
# except Exception as a:
#     print(a)

# deleted data

# delete_data="delete from freiend where id=9"
# try:
#     cr.execute(delete_data)
#     db_conector.commit()
#     print("Data Deleted")
# except Exception as a:
#     print(a)

# fetch data

fetch_data="select * from freiend"
try:
    cr.execute(fetch_data)
    # data=cr.fetchone()
    # data=cr.fetchmany(2)
    data=cr.fetchall()
    print(data)
except Exception as a:
    print(a)