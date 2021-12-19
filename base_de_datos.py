import sqlite3

conn = sqlite3.connect('diccionario_slang.db')
conn.execute('CREATE TABLE diccionario (palabra TEXT, significado TEXT)')
conn.close()