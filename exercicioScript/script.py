#!/usr/bin/python


import sqlite3
import sys

con = sqlite3.connect('test.db')

with con:
    cur = con.cursor()   

    cur.execute("CREATE TABLE Exercise(first TEXT)")
    for i in range(0, 100):
        column = 'c{}'.format(i)
        cur.execute("ALTER TABLE Exercise ADD COLUMN '%s' 'text'" % column)
    for i in range(0, 100):
        cur.execute("INSERT INTO Exercise (c{}, c{}) VALUES('X','X')".format(i, 99-i))
