import sqlite3
from sqlite3.dbapi2 import Cursor

banco = sqlite3.connect('Primeiro banco de dados!')

cursor = banco.cursor()

cursor.execute("INSERT INTO pessoa VALUES('Kauan',40,'kyuri887@gmail.com')")

banco.commit()
cursor.execute('SELECT * FROM pessoa')
print(cursor.fetchall())
