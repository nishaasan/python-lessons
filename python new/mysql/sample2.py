import mysql.connector as mysql

# Establishing connection to MySQL server
conn1 = mysql.connect(host="localhost", user="root", password="123456")

# Creating a cursor object to execute SQL queries
cursor = conn1.cursor()

# Executing SQL query to create a new database
# cursor.execute("CREATE DATABASE demosqlnew")
cursor.execute("USE demosqlnew")

# create_table_query = """
# CREATE TABLE employee (
#     emp_id INT PRIMARY KEY,
#     empname VARCHAR(255),
#     designation VARCHAR(255),
#     location VARCHAR(255)
# )
# """

# cursor.execute(create_table_query)
# sql="insert into employee values (1,'Anisha','SQLAnalyst','India')"
# cursor.execute(sql)

# sql1="update employee set empname='Nisha' where emp_id=1"
# cursor.execute(sql1)

sql2="delete from employee where emp_id=1"
cursor.execute(sql2)
# Committing the transaction
conn1.commit()

# Closing the cursor and connection
cursor.close()
conn1.close()
