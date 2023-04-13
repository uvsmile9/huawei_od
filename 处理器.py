# -*- coding = utf-8 -*-
# @Time : 2023/4/12 17:17
# @Author : uvsmile9
# @File :处理器.py
# @Software : PyCharm
import copy

arr = eval(input())
num = int(input())


def getresult(arr, num):
    link1 = []
    link2 = []
    arr.sort()
    for e in arr:
        if e < 4:
            link1.append(e)
        else:
            link2.append(e)

    ans = []
    len1 = len(link1)
    len2 = len(link2)
    if num == 1:
        if len1 == 1 or len2 == 1:
            if len1 == 1:
                dfs(link1, 0, 1, [], ans)
            if len2 == 1:
                dfs(link2, 0, 1, [], ans)
        if len1 == 3 or len2 == 3:
            if len1 == 3:
                dfs(link1, 0, 1, [], ans)
            if len2 == 3:
                dfs(link2, 0, 1, [], ans)
        if len1 == 2 or len2 == 2:
            if len1 == 2:
                dfs(link1, 0, 1, [], ans)
            if len2 == 2:
                dfs(link2, 0, 1, [], ans)
        if len1 == 4 or len2 == 4:
            if len1 == 4:
                dfs(link1, 0, 1, [], ans)
            if len2 == 4:
                dfs(link2, 0, 1, [], ans)
    elif num == 2:
        if len1 == 2 or len2 == 2:
            if len1 == 2:
                dfs(link1, 0, 2, [], ans)
            if len2 == 2:
                dfs(link2, 0, 2, [], ans)
        if len1 == 4 or len2 == 4:
            if len1 == 4:
                dfs(link1, 0, 2, [], ans)
            if len2 == 4:
                dfs(link2, 0, 2, [], ans)
        if len1 == 3 or len2 == 3:
            if len1 == 3:
                dfs(link1, 0, 2, [], ans)
            if len2 == 3:
                dfs(link2, 0, 2, [], ans)
    elif num == 4:
        if len1 == 4 or len2 == 4:
            if len1 == 4:
                ans.append(link1)
            if len2 == 4:
                ans.append(link2)
    elif num == 8:
        if len1 == 4 and len2 == 4:
            tmp = []
            tmp.extend(link1)
            tmp.extend(link2)
            ans.append(tmp)
    return ans


def dfs(arr, index, level, path, res):
    if len(path) == level:
        res.append(copy.deepcopy(path))
    for i in range(index, len(arr)):
        path.append(arr[i])
        dfs(arr, i + 1, level, path, res)
        path.pop()


print(getresult(arr, num))
