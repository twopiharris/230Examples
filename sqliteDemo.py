""" SQLiteDemo
    Demonstrate building and using
    a database in SQLite
"""

import sqlite3

#build connection to database
conn = sqlite3.connect("practice.db")
c = conn.cursor()

#create a table
c.execute("DROP TABLE IF EXISTS contacts")
sql = """
CREATE TABLE contacts (
  id INTEGER PRIMARY KEY,
  name VARCHAR(20),
  company VARCHAR(20),
  email VARCHAR(20)
) """
c.execute(sql)

#insert records into the table
c.execute("INSERT INTO contacts VALUES (null, ?, ?, ?)",
          ('Andy Harris', 'IUPUI', 'aharris@cs.iupui.edu'))
c.execute("INSERT INTO contacts VALUES (null, ?, ?, ?)",
          ('Bill Gates', 'Microsoft', 'bill@vista.com'))
c.execute("INSERT INTO contacts VALUES (null, ?, ?, ?)",
          ('Steve Jobs', 'Apple', 'steve@newton.com'))

#view the results
result = c.execute("SELECT * FROM contacts")

#get the field names
names = [description[0] for description in result.description]

for record in result:
  fieldNum = 0
  for field in record:
    print ("{:10}: {}".format(names[fieldNum], field))
    fieldNum += 1
  print ("")

#make changes permanent
conn.commit()
c.close()