import sqlite3

conn = sqlite3.connect('user.db')

c = conn.cursor()

# Create table
c.execute('''CREATE TABLE users_data
             (name text not null,
             age int not null,
             hobbies text,
             address text)''')
# c.execute('select * from users_data')

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()