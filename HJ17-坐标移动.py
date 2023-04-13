# -*- coding = utf-8 -*-
# @Time : 2023/4/13 16:05
# @Author : uvsmile9
# @File :HJ17-坐标移动.py
# @Software : PyCharm
input_l = input().split(';')
init_p = [0, 0]

for i in input_l:
    if not 2 <= len(i) <= 3:
        continue
    try:
        d = i[0]
        s = int(i[1:])
        if d in ['A', 'W', 'S', 'D']:
            if 0 <= s <= 99:
                if d == 'A':
                    init_p[0] -= s
                elif d == 'D':
                    init_p[0] += s
                elif d == 'W':
                    init_p[1] += s
                elif d == 'S':
                    init_p[1] -= s
    except:
        continue

print(str(init_p[0]) + ',' + str(init_p[1]))