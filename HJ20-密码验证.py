# -*- coding = utf-8 -*-
# @Time : 2023/4/13 17:53
# @Author : uvsmile9
# @File :HJ20-密码验证.py
# @Software : PyCharm
def check_p(s:str):
    if len(s)<=8:
        return False
    a,b,c,d=0,0,0,0
    for i in s:
        if ord('a')<=ord(i)<=ord('z'):
            a=1
        elif ord('A')<=ord(i)<=ord('Z'):
            b=1
        elif ord('0')<=ord(i)<=ord('9'):
            c=1
        else:
            d=1
    if a+b+c+d<3:
        return False
    for i in range(len(s)-3):
        if len(s.split(s[i:i+3]))>=3:
            return False
    return True

while True:
    try:
        print('OK' if check_p(input()) else 'NG')
    except:
        break