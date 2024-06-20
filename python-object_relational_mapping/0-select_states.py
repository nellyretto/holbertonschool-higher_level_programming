#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == '__main__':
    """
    Connects to a MySQL database and selects all rows from the 'states' table.
    Prints each row in the result set.
    """

    # Connect to the MySQL database
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    # Create a cursor object to execute SQL queries
    cur = db.cursor()

    # Execute the SQL query to select all rows from the 'states' table
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all rows from the result set
    query_rows = cur.fetchall()

    # Print each row in the result set
    for row in query_rows:
        print(row)

    # Close the cursor and database connection
    cur.close()
    db.close()
