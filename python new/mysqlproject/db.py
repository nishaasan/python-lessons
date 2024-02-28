import mysql.connector
class DB:
    def __init__(self):
        try:
            self.conn=mysql.connector.connect(host='localhost', user='root', password='123456',database='demosqlnew')
            self.cursor=self.conn.cursor()
            self.cursor.execute('''create table if not exists demo1(id integer primary key,
                                sname varchar(20),
                                grade varchar(20),
                                DOB Date)''')
            self.conn.commit()
            print("Table created")
        except mysql.connector.Error as e:
            print(e)
            
          
    
    
            