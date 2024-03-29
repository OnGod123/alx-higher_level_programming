#!/usr/bin/python3

import MySQLdb

# Establish connection to the MySQL database
conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")

# Create a cursor object to execute SQL queries
cur = conn.cursor()

# Execute a SELECT query to retrieve all records from the 'states' table
cur.execute("SELECT * FROM states ORDER BY id ASC")

# Fetch all rows returned by the SELECT query
query_rows = cur.fetchall()

# Print each row fetched from the database
for row in query_rows:
    print(row)

# Close the cursor and connection
cur.close()
conn.close()

