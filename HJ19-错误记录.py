# -*- coding = utf-8 -*-
# @Time : 2023/4/13 17:35
# @Author : uvsmile9
# @File :HJ19-错误记录.py
# @Software : PyCharm
l1 = []
l2 = []
while True:
    try:
        s = input().split('\\')[-1]
        d = s.split(' ')[0][-16:] + ' ' + s.split(' ')[1]
        if d not in l1:
            l1.append(d)
            l2.append(1)
        else:
            l2[l1.index(d)] += 1
    except:
        break

for i in range(len(l1[-8:])):
    print(l1[-8:][i], l2[-8:][i])