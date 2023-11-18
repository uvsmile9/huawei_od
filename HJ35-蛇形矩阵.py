#!/usr/bin/env python
# -*- coding = utf-8 -*-
# @Time : 2023/4/14 19:42
# @Author : uvsmile9
# @Project: huawei_od
# @File :HJ35-蛇形矩阵.py
# @Software : PyCharm
# @Desc    :

while True:
    try:
        n=int(input())
        s=sum(range(n+1))
        L=[[] for _ in range(n)]
        while s>0:
            for i in range(n):
                L[i].append(str(s-i))
            s-=n
            n-=1
        for i in L:
            print(' '.join(i[::-1]))
    except:
        break
