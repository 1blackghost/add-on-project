import sqlite3

def reset_back_to_start():
    '''
    table gets reseted to original data.
    maybe copy and saved data before resetting it,? it may have use.
    '''
    # Connect to database
    conn = sqlite3.connect('mydb.db')
    c = conn.cursor()

    print("[WARNING!] You need admin privilege to clear and reset the data! Are you sure? (y/n/yes/no)")
    a = input()
    c.execute("DROP TABLE IF EXISTS users")
    if a == "y" or a == "yes":
        c.execute('''CREATE TABLE IF NOT EXISTS users
                    (uid INTEGER PRIMARY KEY AUTOINCREMENT,
                     t TEXT NOT NULL,
                     m INTEGER NOT NULL,
                     am_pm TEXT NOT NULL,
                     price TEXT NOT NULL
                     )''')

    conn.commit()

    # Close connection
    c.close()
    conn.close()


def update_this(uid, t=None, m=None, am_pm=None, price=None):
    conn = sqlite3.connect('mydb.db')
    c = conn.cursor()

    update_fields = []
    update_values = []
    if t:
        update_fields.append("t = ?")
        update_values.append(t)
    if m:
        update_fields.append("m = ?")
        update_values.append(m)
    if am_pm:
        update_fields.append("am_pm = ?")
        update_values.append(am_pm)
    if price is not None:
        update_fields.append("price = ?")
        update_values.append(price)

    if len(update_fields) > 0:
        update_query = "UPDATE users SET " + ",".join(update_fields) + " WHERE uid = ?"
        update_values.append(uid)
        c.execute(update_query, tuple(update_values))
        conn.commit()
    conn.close()


def insert_this(t="", m="", am_pm="", price=0):
    '''
    values can be appended to the db using this , any unpassed arguments results in activation
    of keyword arguments
    returns its uuid : int
    '''
    # Connect to database
    conn = sqlite3.connect('mydb.db')
    c = conn.cursor()

    c.execute("INSERT INTO users (t, m, am_pm, price) VALUES (?, ?, ?, ?)", (t, m, am_pm, price))
    uid = c.lastrowid
    conn.commit()

    # Close connection
    c.close()
    conn.close()

    return uid


def read_for(uid=-1):
    '''
    Reads data for certain uuids : returnType: str
    '''
    # Connect to database
    conn = sqlite3.connect('mydb.db')
    c = conn.cursor()

    if uid != -1:
        c.execute("SELECT * FROM users WHERE uid = ?", (uid,))
        result = str(c.fetchone())

    else:
        c.execute("SELECT * FROM users")
        result = c.fetchall()



    # Close
    c.close()
    conn.close()

    return result
