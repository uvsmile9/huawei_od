# -*- coding = utf-8 -*-
# @Time : 2023/4/13 11:29
# @Author : uvsmile9
# @File :HJ16-购物单.py
# @Software : PyCharm
#
# n, m = map(int, input().split())
# primary, annex = {}, {}
# for i in range(1, m + 1):
#     x, y, z = map(int, input().split())
#     if z == 0:
#         primary[i] = [x, y]
#     else:
#         if z in annex:
#             annex[z].append([x, y])
#         else:
#             annex[z] = [[x, y]]
# m = len(primary)
# dp = [[0] * (n + 1) for _ in range(m + 1)]
# w, v = [[]], [[]]
# for key in primary:
#     w_temp, v_temp = [], []
#     w_temp.append(primary[key][0])
#     v_temp.append(primary[key][0] * primary[key][1])
#     if key in annex:
#         w_temp.append(w_temp[0] + annex[key][0][0])
#         v_temp.append(v_temp[0] + annex[key][0][0] * annex[key][0][1])
#         if len(annex[key]) > 1:
#             w_temp.append(w_temp[0] + annex[key][1][0])
#             v_temp.append(v_temp[0] + annex[key][1][0] * annex[key][1][1])
#             w_temp.append(w_temp[0] + annex[key][0][0] + annex[key][1][0])
#             v_temp.append(v_temp[0] + annex[key][0][0] * annex[key][0][1] + annex[key][1][0] * annex[key][1][1])
#     w.append(w_temp)
#     v.append(v_temp)
#
# for i in range(1, m + 1):
#     for j in range(10, n + 1, 10):
#         max_i = dp[i - 1][j]
#         for k in range(len(w[i])):
#             if j - w[i][k] >= 0:
#                 max_i = max(max_i, dp[i - 1][j - w[i][k]] + v[i][k])
#         dp[i][j] = max_i
# print(dp[m][n])

n, m = map(int, input().split())
dict1, dict2 = {}, {}
for i in range(1, m + 1):
    v, p, q = map(int, input().split())
    if q == 0:
        dict1[i] = [v, p]
    else:
        if q in dict2:
            dict2[q].append([v, p])
        else:
            dict2[q] = [[v, p]]
dp = [0] * (n + 1)
for key in dict1:
    w, v = [], []
    w.append(dict1[key][0])
    v.append(dict1[key][0] * dict1[key][1])
    if key in dict2:
        w.append(w[0] + dict2[key][0][0])
        v.append(v[0] + dict2[key][0][0] * dict2[key][0][1])
        if len(dict2[key]) > 1:
            w.append(w[0] + dict2[key][1][0])
            v.append(v[0] + dict2[key][1][0] * dict2[key][1][1])
            w.append(w[0] + dict2[key][0][0] + dict2[key][1][0])
            v.append(v[0] + dict2[key][0][0] * dict2[key][0][1] + dict2[key][1][0] * dict2[key][1][1])
    for j in range(n, -1, -10):
        for k in range(len(w)):
            if j - w[k] >= 0:
                dp[j] = max(dp[j], dp[j - w[k]] + v[k])

print(dp[n])
