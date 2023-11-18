# -*- coding = utf-8 -*-
# @Time : 2023/4/13 21:22
# @Author : uvsmile9
# @File :HJ26-字符串排序.py
# @Software : PyCharm
# while True:
#     try:
#         s=input()
#         a=''
#         for i in s:
#             if i.isalpha():
#                 a+=i
#         b=sorted(a,key=str.upper)
#         index=0
#         d=''
#         for i in range(len(s)):
#             if s[i].isalpha():
#                 d+=b[index]
#                 index+=1
#             else:
#                 d+=s[i]
#         print(d)
#     except:
#         break