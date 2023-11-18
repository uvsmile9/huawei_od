# -*- coding = utf-8 -*-
# @Time : 2023/4/13 19:53
# @Author : uvsmile9
# @File :HJ23-删最少字符.py
# @Software : PyCharm

while True:
    try:
        s=input()
        dic={}
        res=''
        for c in s:
            if c not in dic:
                dic[c]=1
            else:
                dic[c]+=1
        minc=min(dic.values())
        for c in s:
            if dic[c]!=minc:
                res+=c
        print(res)
    except:
        break