# -*- coding = utf-8 -*-
# @Time : 2023/4/13 18:09
# @Author : uvsmile9
# @File :HJ21-简单密码.py
# @Software : PyCharm
while True:
    try:
        s = input()
        res = []
        for i in s:
            if i.isdigit():
                res.append(i)
            elif i.isupper() and i != 'Z':
                res.append(chr(ord(i.lower()) + 1))
            elif i == 'Z':
                res.append('a')
            else:
                if i in 'abc':
                    res.append('2')
                elif i in 'def':
                    res.append('3')
                elif i in 'ghi':
                    res.append('4')
                elif i in 'jkl':
                    res.append('5')
                elif i in 'mno':
                    res.append('6')
                elif i in 'pqrs':
                    res.append('7')
                elif i in 'tuv':
                    res.append('8')
                elif i in 'wxyz':
                    res.append('9')
        print(''.join(res))
    except:
        break
