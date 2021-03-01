import sqlite3

conn  = sqlite3.connect('a.db')   # create a.db if it not exist

c = conn.cursor()

c.execute("SELECT * FROM users")

print(c.fetchone())

print(c.fetchmany(3))

print(c.fetchall())



conn.commit()
conn.close()
