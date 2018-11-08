import sqlite3

connection = sqlite3.connect('data.db') # sql lite contains everything in a file

cursor = connection.cursor() # allows you to select things

create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)

user = (1, 'jose', 'asdf')
insert_query = "INSERT INTO users VALUES (?,?,?)"
cursor.execute(insert_query, user) # replace things within tuple for the question marks 

users = [
    (2, 'jose', 'asdf'),
    (3, 'jose', 'asdf'),
    (4, 'jose', 'asdf')
]

cursor.executemany(insert_query, users)

select_query = "SELECT * FROM users"

for row in cursor.execute(select_query):
    print(row)

connection.commit() # save changes into data.db file
connection.close()