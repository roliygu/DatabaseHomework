#! /usr/bin/env python
#coding=utf-8
import random

def passwordCreate(a):
    t=random.randint(2,9)
    B=str(t)
    for i in a:
        b = ord(i) * t % 127
        if b<10:
            B+='00'
            B+=str(b)
        elif b<100:
            B+='0'
            B+=str(b)
        else:
            B+=str(b)
    return B
 

def div(t,b):
    k=0
    a=(k*127 + b)/t
    while a < 48 or a*t-b!=k*127:
        k+=1
        a=(k*127 + b)/t
    plice=chr(a)
    return plice
          

def decode(code):
    t=int(code[0])
    i=1
    A=''
    while i <= len(code)-2:
        B=code[i:i+3]
        i+=3
        num=int(B)
        A+=div(t,num)
    return A
        
