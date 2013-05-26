#! /usr/bin/env python
#coding=utf-8
import os
import MySQLdb
conn = MySQLdb.Connect(user='root',passwd='KF.moon083166139339',db='text')

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

def SQLCarryout(s):
	if len(s)<5:
		print "SQLinput is illegality!"
	else:
		cou=conn.cursor()
		cou.execute(s)
		return cou
	
def SQL():
	s=SQLinput()
	cu=SQLCarryout(s)
	show(cu)
	
def SQLcreate():
	SQL_text = open('G:\DatabaseHomework\datacreate.txt','r')
	SQLcre = SQL_text.readlines()
	for i in SQLcre:
		SQLCarryout(i)

SQL()
x=input("a")
coursor.close()
conn.close()

