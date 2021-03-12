import psycopg2

def createTable():
    con = psycopg2.connect("dbname='data2' user='postgres' password='postpost' port='5432' host='localhost' ")
    cur = con.cursor()
    cur.execute("CREATE TABLE data (rollno INTEGER, name TEXT, marks REAL)")
    con.commit()
    con.close()


def insert(roll,name,mark):
    con = psycopg2.connect("dbname='data2' user='postgres' password='postpost' port='5432' host='localhost' ")
    cur = con.cursor()
    cur.execute("INSERT INTO data VALUES(%s,%s,%s)",(roll,name,mark))
    con.commit()
    con.close()

def view():
    con = psycopg2.connect("dbname='data2' user='postgres' password='postpost' port='5432' host='localhost' ")
    cur = con.cursor()
    cur.execute("SELECT * FROM data")
    rows = cur.fetchall()
    con.commit()
    con.close()
    return rows

def delete(name):
    con = psycopg2.connect("dbname='data2' user='postgres' password='postpost' port='5432' host='localhost' ")
    cur = con.cursor()
    cur.execute("DELETE FROM data WHERE name=%s", (name,))  
    con.commit()
    con.close()

def update(roll,name,mark):
    con = psycopg2.connect("dbname='data2' user='postgres' password='postpost' port='5432' host='localhost' ")
    cur = con.cursor()
    cur.execute("UPDATE data SET name=%s, marks=%s WHERE rollno=%s",(name,mark,roll))  
    con.commit()
    con.close()


#createTable()
#insert(1,'cat',70.0)
#insert(1,'cat',70.0)
#insert(3,'parrot',75.0)
#insert(4,'snake',80.0)

#print(view())

#delete('parrot')

update(2,'bird',84.0)