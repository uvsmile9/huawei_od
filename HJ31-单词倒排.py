#!/usr/bin/env python
# -*- coding = utf-8 -*-
# @Time : 2023/4/14 17:16
# @Author : uvsmile9
# @Project: huawei_od
# @File :HJ31-单词倒排.py
# @Software : PyCharm
# @Desc    :

while True:
    try:
        a=input()
        for i in a:
            if not i.isalpha():
                a=a.replace(i,' ')
            b=a.split()
        print(*b[::-1])
    except:
        break
