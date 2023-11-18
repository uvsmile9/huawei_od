# -*- coding = utf-8 -*-
# @Time : 2023/4/14 08:26
# @Author : uvsmile9
# @File :HJ28-素数伴侣.py
# @Software : PyCharm

#
# def is_prime(num):
#     """判断是否为素数，偶数无需判断"""
#     for i in range(3, int(num ** 0.5) + 2, 2):
#         if num % i == 0:
#             return False
#     return True
#
#
# def group_list(num_list):
#     """分奇偶：因为素数一定是奇数+偶数"""
#     odds, evens = [], []
#     for num in num_list:
#         if num % 2 == 0:
#             evens.append(num)
#         else:
#             odds.append(num)
#     return odds, evens
#
#
# def matrix_oe(odds, evens):
#     """奇偶伴侣矩阵，找到所有可能的伴侣组合"""
#     l = [[0 for _ in evens] for _ in odds]
#     for oi, ov in enumerate(odds):
#         for ei, ev in enumerate(evens):
#             if is_prime(ov + ev):
#                 l[oi][ei] = 1
#     return l
#
#
# def find(oi, evens, matrix, used_e, connect_e):
#     """为每个奇数找合适的伴侣"""
#     for ei in range(len(evens)):
#         # 如果奇偶适合则进一步判断
#         if matrix[oi][ei] == 1 and used_e[ei] == 0:
#             used_e[ei] = 1
#             # 难点：如果当前偶数还没有配对或者当前偶数的原配奇数可以找到其他的偶数伴侣
#             if connect_e[ei] == -1 or find(connect_e[ei], evens, matrix, used_e, connect_e):
#                 connect_e[ei] = oi
#                 return 1
#     return 0
#
#
# data = [line.strip() for line in sys.stdin]
# n = len(data)
# for i in range(0, n, 2):
#     num_list = [int(s) for s in data[i + 1].split(" ")]
#     odds, evens = group_list(num_list)
#     matrix = matrix_oe(odds, evens)
#     connect_e = [-1 for _ in evens]
#     count = 0
#     for oi in range(len(odds)):
#         used_e = [0 for _ in range(len(evens))]
#         if find(oi, evens, matrix, used_e, connect_e):
#             count += 1
#     print(count)
#
#
import math
def check_s(num):
    for i in range(2, int(math.sqrt(num)) + 2):
        if (num % i == 0):
            return False
    return True


def find(odd, visited, choose, evens):
    for j, even in enumerate(evens):
        if check_s(odd + even) and not visited[j]:
            visited[j] = True
            if choose[j] == 0 or find(choose[j], visited, choose, evens):
                choose[j] = odd
                return True
    return False


while True:
    try:
        num = int(input())
        li = list(map(int, input().split()))
        evens = []
        odds = []
        count = 0
        for i in li:
            if i % 2 == 0:
                odds.append(i)
            else:
                evens.append(i)
        choose = [0] * len(evens)
        for odd in odds:
            visited = [False] * len(evens)
            if find(odd, visited, choose, evens):
                count += 1
        print(count)
    except:
        break
