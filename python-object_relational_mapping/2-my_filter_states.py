#!/usr/bin/python3

"""
    Connects to a MySQL database and retrieves all rows from the 'states' table
    where the name matches the provided name parameter.

    Args:
        name (str): The name to filter the states by.

    Returns:
        None
    """
import MySQLdb
import sys

if __name__ == '__main__':

    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])

    cur = db.cursor()

    cur.execute(
        "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY "
        "states.id ASC".format(sys.argv[4],))

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
