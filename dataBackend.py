import sqlite3

def connect():
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS routine (id INTEGER PRIMARY KEY, date TEXT, earnings INTEGER, exercise TEXT, study TEXT, diet TEXT, python TEXT)")
    conn.commit()
    conn.close()

def insert(date, earnings, exercise, study, diet, python):
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO routine VALUES (NULL, ?, ?, ?, ?, ?, ?)", (date , earnings , exercise, study, diet, python))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM routine")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM routine WHERE id=?", (id,))
    conn.commit()
    conn.close()

def search(date='', earnings='', exercise='', study='', diet='', python=''):
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM routine WHERE date=?  OR earnings=? OR exercise=? OR study=? OR diet=? OR python=?" , (date , earnings , exercise , study , diet , python))
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

#print(search(date='04-01-2019'))



#connect()
#insert('01-01-2019',100,'did exercise','did study','diet taken', 'did python')
#insert('04-01-2019',200,'did exercise','did not study','diet taken', 'did python')
#insert('05-01-2019',300,'did not exercise','did study','diet taken', 'did python')
#print(view())
#delete(2)