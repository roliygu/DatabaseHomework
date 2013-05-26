#! /usr/bin/env python
#coding=utf-8
import sys
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
    return dic

def checkcode():
    fir_code=raw_input("please input your password first : ")
    sec_code=raw_input("please input your password second : ")
    if fir_code==sec_code:
        return fir_code
    else:
         return 0
    
def main():
    k=input("Had an username(1) or no(2) or quit(3)?:")
    if k == 3:
        return 0
    elif k == 1:
        name=raw_input("what is your username? :")
        code=raw_input("what is your password? :")
        d=makedic()
        co=d.get(name)[0]
        if co!=None and decode(co)==code:
            return 1
        else:
            print "your username or password is error!"
            main()
    elif k==2:
        newcode=check()
        if newcode == 0:
            print "your two times inputs are different!please try it again"
            newcode=check()
        else:
            s=
            
        
        