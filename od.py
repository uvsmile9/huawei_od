#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 13:22:32 2023

@author: uvsmile9
"""

import sys


# HJ2

# a,b=[i.strip() for i in sys.stdin]
# print(a.lower().count(b.lower()))

# while True:
#     try:
#         a=str(input()).upper()
#         b=input().upper()
#         res=0
#         for i in a:
#             if i==b:
#                 res+=1
#         print(res)
#     except:
#         break

# HJ3

# while True:
#     try:
#         n=input()
#         list=[]
#         for i in range(int(n)):
#             list.append(int(input()))
#         uniq=set(list)
#         for j in sorted(uniq):
#             print(j)
#     except:
#         break

# HJ4

# while True:
#     try:
#         l=input()
#         for i in range(0,len(l),8):
#             print("{0:0<8s}".format(l[i:i+8]))
#     except:
#         break

# while True:
#     try:
#         t=input()
#         while(len(t)>0):
#             print(t[:8].ljust(8,'0'))
#             t=t[8:]
#     except:
#         break

# HJ5
# while True:
#     try:
#         s=input()
#         print(int(s,l6))
#     except:
#         break

# while True:
#     try:
#         s=input()[2:]
#         l=len(s)
#         dic={'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
#         c=0
#         for i in s:
#             if i in dic:
#                 c+=dic[i]*16**(l-1)
#                 l-=1
#             else:
#                 c+=int[i]*16**(l-1)
#                 l-=1
#         print(c)
#     except:
#         break

#HJ6

# import math
# n=int(input())
# for i in range(2,int(math.sqrt(n))+1):
#     while n%i==0:
#         print(i,end=' ')
#         n=n//i 
# if n>2:
#     print(n)
    
#HJ7

# a=float(input())
# if a%1 >=0.5:
#     a+=0.5
# print(int(a))

#HJ8
# n=int(input())
# dic={}
# for i in range(n):
#     line=input().split()
#     key=int(line[0])
#     value=int(line[1])
#     dic[key]=dic.get(key,0)+value

# for j in sorted(dic):
#     print(j,dic[j])

#HJ9
# while True:
#     try:
#         s=input()
#         if (s[-1] !='0'):
#             ns=s[::-1]
#         n=[]
#         for i in ns:
#             if i in n:
#                 continue
#             else:
#                 n.append(i)
#                 print(i,end='')   
#     except:
#         break

#HJ10
# print(len(set(input().replace('\n',''))))

#print(len(set(map(lambda x:x,input().replace('\n','')))))

# def char_count(str):
#     s=str.replace('\n','')
#     c=0
#     for i in s:
#         if 0<=ord(i)<=127:
#             c+=1
#     return c
# str=input()
# print(char_count(str))

#HJ13 
# while True:
#     try:
#         s1=input().split()[::-1]
#         print(' '.join(s1))
#     except:
#         break

# HJ14
while True:
    try:
        n=input()
        l=[]
        for i in range(int(n)):
            l.append(input())
        print('\n'.join(sorted(l)))
    except:
        break