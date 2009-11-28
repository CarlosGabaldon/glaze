#!/usr/bin/python

import MySQLdb

def execute_sql(sql):
    try:
        db = MySQLdb.connect("localhost","root","","Glaze" )
        cursor = db.cursor()
        cursor.execute(sql)
        return cursor.fetchall()
        
    except Exception, e: # in 3.1; except Exception as e:
        print e

    db.close()

