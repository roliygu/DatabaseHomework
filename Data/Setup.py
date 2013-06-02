#! /usr/bin/env python
#coding=utf-8
import sys
import MySQLdb
import getpass

def SQLcreate():
	SQL_text = open('G:\DatabaseHomework\data\datacreate.txt','r')
	SQLcre = SQL_text.readlines()
	for i in SQLcre:
		SQLCarryout(i)
	SQL_text.close()
	conn.commit()

def SQLCarryout(s):
	if len(s)<5:
		print "SQLinput is illegality!"
	else:
		cou=conn.cursor()
		cou.execute(s)
		return cou

def checkcode():
    fir_code=getpass.getpass("please input your password first : ")
    sec_code=getpass.getpass("please input your password second : ")
    if fir_code==sec_code:
        return fir_code
    else:
        return 0
	
def getCode():
    User=open('G:\DatabaseHomework\data\UserCode.txt','r')
    User_code=User.readlines()
    if User_code != []:
        User_code=User_code[0]
        User.close()
        return 0
    else :
        User_code=checkcode()
        if User_code==0:
            print "your two times inputs are different!please try it again"
            User_code=checkcode()
        else :
            out = open('G:\DatabaseHomework\data\UserCode.txt','w')
            out.write(User_code)
            out.close()
        return User_code
            
def LinkandCreate(code):
    conn = MySQLdb.Connect(user='root',passwd=code)   
    return conn
 
code=getCode()
if code !=0:
    conn=LinkandCreate(code)
    SQLcreate()
    print " Made it !!"
else :
	User=open('G:\DatabaseHomework\data\UserCode.txt','r')
	code=User.readlines()
	User.close()
	code=code[0]
	conn=LinkandCreate(code)
	sql="use student_takes;"
	cou=conn.cursor()
	n=cou.execute(sql)
	print "It had been setup"

def Add_one(gra,ID,course_ID,yea):
	ex=('takes',gra,ID,course_ID,yea)
	sql="insert into %s values (%s,%s,%s,%s);" % ex
	cou=conn.cursor()
	n=cou.execute(sql)
	conn.commit()
	return n


def Add_mul(L):
	for i in L:
		i=i.split(" ")
		ex_id=i[0]
		ex_course_id=i[1]
		ex_gra=i[2]
		ex_yea=i[3]
		Add_one(ex_gra,ex_id,ex_course_id,ex_yea)
		

def SQLCarryout_mul(L):
	L=L[:-1]
	print L
	for i in L:
		i+=";"
		SQLCarryout(i)
		conn.commit()	

def get_all(ex_yea,ex_course_id):
	ex=(ex_yea,ex_course_id)
	sql="select ID,grade from takes where years=%s and course_ID=%s;" %ex
	cous=SQLCarryout(sql)
	a=cous.fetchall()
	return a	
