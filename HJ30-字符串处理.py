#!/usr/bin/env python
# -*- coding = utf-8 -*-
# @Time : 2023/4/14 16:50
# @Author : uvsmile9
# @Project: huawei_od
# @File :HJ30-字符串处理.py
# @Software : PyCharm
# @Desc    :

import re
def trans(x):
    if re.search(r'[0-9A-Fa-f]',x):
        return hex(int(bin(int(x,16))[2:].rjust(4,'0')[::-1],2))[2:].upper()
    else:
        return x

while True:
    try:
        s1,s2=input().split()
        s=list(s1+s2)
        s[::2]=sorted(s[::2])
        s[1::2]=sorted(s[1::2])
        res=''
        for i in s:
            res+=trans(i)
        print(res)
    except:
        break


