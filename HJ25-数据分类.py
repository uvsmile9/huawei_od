# -*- coding = utf-8 -*-
# @Time : 2023/4/13 20:42
# @Author : uvsmile9
# @File :HJ25-数据分类.py
# @Software : PyCharm
while True:
    try:
        a = input().split()[1:]
        b = map(str, sorted(map(int, set(input().split()[1:]))))
        res = ''
        ttn = 0
        for n in b:
            r1 = ''
            c1 = 0
            for i, v in enumerate(a):
                if n in v:
                    r1 += str(i) + ' ' + v + ' '
                    c1 += 1
                    ttn += 2
            if c1>0:
                r1 = n + ' ' + str(c1) + ' ' + r1
                ttn += 2
            res += r1
        print((str(ttn) + ' ' + res).rstrip())
    except:
        break
