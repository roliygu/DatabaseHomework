#! /usr/bin/env python
#coding=utf-8
import sys
import getpass
sys.path+=["G:\DatabaseHomework"]
from Code import *

def makedic():
    dic={}
    user_text = open('G:\DatabaseHomework\Userlist.txt','r')
    userlist = user_text.readlines()
    for i in userlist:
        t = i.split(' ')
        dic_x={t[0]:[t[1],t[2]]}
        dic.update(dic_x)
    user_text.close()
    return dic

def checkcode():
    fir_code=getpass.getpass("please input your password first : ")
    sec_code=getpass.getpass("please input your password second : ")
    if fir_code==sec_code:
        return fir_code
    else:
         return 0
    
def main():
    k=input("Had an username(1) or no(2) or quit(3)?:")
    while k==1 or k==2 or k==3:
        if k == 3:
            return 0
        elif k==1:
            name=raw_input("what is your username? :")
            code=getpass.getpass("what is your password? :")
            d=makedic()
            co=d.get(name)[0]
            if co!=None and decode(co)==code:
                return 1
            else:
                print "your username or password is error!"
                k=input("Had an username(1) or no(2) or quit(3)?:")
        elif k==2:
            newusername=raw_input("please input your new userneme : ")
            newcode=checkcode()
            if newcode == 0:
                print "your two times inputs are different!please try it again"
                newcode=checkcode()
            else:
                s=passwordCreate(newcode)
                out = open('G:\DatabaseHomework\Userlist.txt','a+')
                out.write(newusername)
                out.write(" ")
                out.write(s)
                out.write(" ")
                out.write("0000000")
                out.write('\n')
                out.close()
                print "Create successfully!"
            k=input("Had an username(1) or no(2) or quit(3)?:")

main()