import sqlite3 

def createTable():
    con = sqlite3.connect('lite.db')
    cur = con.cursor()
    cur.execute("CREATE TABLE data(rollno INTEGER, name TEXT, marks REAL)")
    con.commit()
    con.close()

#createTable()

def insert(roll,name,mark):
    con = sqlite3.connect('lite.db')
    cur = con.cursor()
    cur.execute("INSERT INTO data VALUES(?,?,?)",(roll,name,mark))
    con.commit()
    con.close()

def view():
    con = sqlite3.connect('lite.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM data")
    rows = cur.fetchall()
    con.commit()
    con.close()
    return rows

def delete(name):
    con = sqlite3.connect('lite.db')
    cur = con.cursor()
    cur.execute("DELETE FROM data WHERE name=?", (name,))  
    con.commit()
    con.close()

def update(roll,name,mark):
    con = sqlite3.connect('lite.db')
    cur = con.cursor()
    cur.execute("UPDATE data SET name=?, marks=? WHERE rollno=?",(name,mark,roll))  
    con.commit()
    con.close()


#insert(3,'dog',66.0)
#print(view())
#delete('dog')
#update(3,'pony',89.3)
