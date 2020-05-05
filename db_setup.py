import sqlite3

conn = sqlite3.connect('database.db')
print("Opened database successfully")
conn.execute('DROP TABLE IF EXISTS students')
print("Table dropped successfully")
conn.execute('CREATE TABLE students ( name TEXT, addr TEXT, city TEXT, pin TEXT)')
# conn.execute('CREATE TABLE verses (sourah TEXT, verse TEXT, txt TEXT)')
print("Table created successfully")
conn.close()