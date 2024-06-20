#!/usr/bin/python3
"""
    Connects to a MySQL database and selects all rows from the 'states' table.
    Prints each row in the result set.
"""
import MySQLdb
import sys


if __name__ == '__main__':

    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()

    cur.execute("SELECT id, name FROM states ORDER BY states.id ASC")

    rows = cur.fetchall()

    for row in rows:
        print(f"{row}")

    cur.close()
    db.close()
