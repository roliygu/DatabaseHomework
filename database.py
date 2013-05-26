#! /usr/bin/env python
#coding=utf-8
import os
import MySQLdb
conn = MySQLdb.Connect(user='root',passwd='KF.moon083166139339',db='text')

def SQLinput():
	s=raw_input('>>')
	while s[-1] is not ';':
		s+=" "
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
	SQL_text.close()
	conn.commit()

def takes_updata():
	grade_text = open('G:\DatabaseHomework\grade.txt','r')
	grade_data=grade_text.readlines()
	for i in grade_data:
		grade=i[0:2]
		ID=i[3:10]
		course_ID=i[11:18]
		years=i[19:]
		ex=('takes',grade,ID,course_ID,years)
		sql="insert into %s values (%s,%s,%s,%s);" % ex
		cou=conn.cursor()
		n=cou.execute(sql)
	conn.commit()
	return n

def delet():
	L=['student','takes','course']
	for i in L:
		sql="drop table %s;" % i
		cou=conn.cursor()
		n=cou.execute(sql)
	conn.commit()
	return n

SQL()
x=input("a")
coursor.close()
conn.close()

