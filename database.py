#! /usr/bin/env python
#coding=utf-8
import os
import MySQLdb
conn = MySQLdb.Connect(user='root',passwd='KF.moon083166139339',db='text')
coursor=conn.cursor()

def SQLinput():
	s=raw_input('>>')
	while s[-1] is not ';':
		s+=' '
		s+=raw_input('->    ')
	return s


def show(coursor):
	a=coursor.fetchall()
	for row in a:
		print(row)


def SQL():
	coursor=conn.cursor()
	s=SQLinput()
	if coursor.execute(s) != 0:
		show(coursor)

SQL()
x=input("a")
coursor.close()
conn.close()

