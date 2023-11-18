# -*- coding = utf-8 -*-
# @Time : 2023/4/13 21:39
# @Author : uvsmile9
# @File :HJ27-查找单词.py
# @Software : PyCharm
while True:
    try:
        l1=input().split()
        n=l1[0]
        k=l1[-1]
        l2=l1[1:-2]
        x=l1[-2]

        m=0
        l3=[]

        for w in l2:
            if w==x:
                continue
            elif sorted(w)==sorted(x):
                m+=1
                l3.append(w)
        print(m)
        l4=sorted(l3)
        print(l4[int(k)-1])
    except:
        break