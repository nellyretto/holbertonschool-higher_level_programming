#!/usr/bin/python3

"""
    This script connects to a MySQL database and retrieves the cities
    and their corresponding states.
    It takes three command-line arguments: the MySQL username, password,
    and database name.
    """

import MySQLdb
import sys

if __name__ == '__main__':

    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()

    cur.execute("SELECT cities.id, cities.name, states.name FROM cities JOIN "
                "states ON cities.state_id = states.id ORDER BY id ASC")

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
