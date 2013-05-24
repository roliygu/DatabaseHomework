#! /usr/bin/env python
#coding=utf-8
import os
import MySQLdb
conn = MySQLdb.Connect(user='root',passwd='KF.moon083166139339',db='text')
coursor=conn.cursor()
coursor.execute('''
	select *
	from student ;''')
for row  in coursor.fetchall():
    print(row)
coursor.close()
conn.close()