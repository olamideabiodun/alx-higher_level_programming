#!/usr/bin/python3
""" Lists all states in the database hbtn_0e_0_usa where name matches the argument provided"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cursor = db.cursor()

    sql = f"SELECT * FROM states WHERE name LIKE '{sys.argv[4]}' ORDER BY id ASC"
    cursor.execute(sql)

    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    db.close()
