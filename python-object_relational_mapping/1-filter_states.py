#!/usr/bin/python3
"""
    Connects to a MySQL database and retrieves all
    states whose name starts with 'N'.
    Prints the retrieved rows.
    """
import MySQLdb
import sys

if __name__ == '__main__':

    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()

    cur.execute(
        "SELECT * FROM states WHERE name like 'N%' ORDER BY states.id ASC")

    rows = cur.fetchall()

    for row in rows:
        if row[1][0]:
            print(row)

    cur.close()
    db.close()
