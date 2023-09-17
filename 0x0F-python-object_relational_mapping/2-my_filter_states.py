#!/usr/bin/python3
"""  script that takes in an argument and displays all values in the states """
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'"
                .format(sys.argv[4]))
    curs = cur.fetchall()
    for i in curs:
        print(i)
    cur.close()
    db.close()
