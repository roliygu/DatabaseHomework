#! /usr/bin/env python
#coding=utf-8
import os
import MySQLdb
conn = MySQLdb.Connect(user='root',passwd='KF.moon083166139339',db='text')
coursor=conn.cursor()
def SQLinput():
	s=raw_input('>>')
	while s[-1] is not ';':
		s+=raw_input('->    ')
	return s
s=SQLinput()
coursor.execute(s)
for row  in coursor.fetchall():
    print(row)
coursor.close()
conn.close()
input()
