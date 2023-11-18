# -*- coding = utf-8 -*-
# @Time : 2023/4/13 19:55
# @Author : uvsmile9
# @File :HJ24-合唱队.py
# @Software : PyCharm
from bisect import bisect_left
def inc_mac(l:list):
    dp=[1]*len(l)
    arr=[l[0]]
    for i in range(1,len(l)):
        if l[i]>arr[-1]:
            arr.append(l[i])
            dp[i]=len(arr)
        else:
            pos=bisect_left(arr,l[i])
            arr[pos]=l[i]
            dp[i]=pos+1
    return dp

while True:
    try:
        nl=int(input())
        sl=list(map(int,input().split()))
        left_s=inc_mac(sl)
        right_s=inc_mac(sl[::-1])[::-1]
        sum_s=[left_s[i]+right_s[i]-1 for i in range(len(sl))]
        print(str(nl-max(sum_s)))
    except:
        break