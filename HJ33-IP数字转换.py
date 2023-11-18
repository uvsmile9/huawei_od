#!/usr/bin/env python
# -*- coding = utf-8 -*-
# @Time : 2023/4/14 19:00
# @Author : uvsmile9
# @Project: huawei_od
# @File :HJ33-IP数字转换.py
# @Software : PyCharm
# @Desc    :
def ip2num(ip:str):
    ip_l=ip.split('.')
    for i in range(len(ip_l)):
        ip_l[i]=bin(int(ip_l[i]))[2:].rjust(8,'0')
    num=int('0b'+''.join(ip_l),2)
    return num

def num2ip(num:int):
    num_l=bin(int(num))[2:].rjust(32,'0')
    bin_l=[num_l[0:8],num_l[8:16],num_l[16:24],num_l[24:]]
    ip_l=list(map(str,[int('0b'+i,2) for i in bin_l]))
    ip='.'.join(ip_l)
    return ip

while True:
    try:
        l1=input()
        l2=int(input())
        print(ip2num(l1))
        print(num2ip(l2))
    except:
        break

