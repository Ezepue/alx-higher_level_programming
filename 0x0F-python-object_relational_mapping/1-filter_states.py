#!/usr/bin/python3
'''
lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
'''

import MySQLdb
from sys import argv

if __name__ == '__main__':
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        charset='utf8'
    )

    curr = conn.cursor()
    query = '''
        SELECT * FROM states
        WHERE name LIKE 'N%'
        ORDER BY id ASC
        '''
    curr.execute(query)

    for row in curr.fetchall():
        print(row)

    curr.close()
    conn.close()
