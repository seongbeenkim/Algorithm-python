#https://www.acmicpc.net/problem/2422

import sys

n, m = map(int,sys.stdin.readline().split())
avoid = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int,sys.stdin.readline().split())
    avoid[x].append(y)
    avoid[y].append(x)

answer = set()

def check(res):

    for x in res:
        cnt = 0
        if len(avoid[x]) > 0:
            cnt += 1
        for i in avoid[x]:
            if i in res:
                cnt += 1
                if cnt >= 2:
                    return False

    return True

def dfs(idx,start,res):
    global answer

    if len(res) == 3:
        if check(res):
            answer.add(tuple(res))
        return

    if idx >= n or start >= n:
        return

    for i in range(start,n):
        dfs(idx+1,i+1,res+[i+1])

dfs(0,0,[])

print(len(answer))