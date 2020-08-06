#https://www.acmicpc.net/problem/16947

import sys
from collections import deque
sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline())
a = [[] for _ in range(n)]

d = [-1] * n
ans = [-1] * n

for _ in range(n):
    u,v = map(int,sys.stdin.readline().split())
    u -= 1
    v -= 1
    a[u].append(v)
    a[v].append(u)

def cycle(start,now,length,candi):
    if check[now]:
        if start == now and length >= 2:
            for i in candi:
                ans[i] = 0
            return True
        else:
            return False

    check[now] = True

    for i in a[now]:
        if not check[i]:
            if cycle(start,i,length+1,candi + [i]):
                return True
        else:
            if i == start and length >= 2:
                if cycle(start, i, length, candi):
                    return True
    return False

def bfs(i):
    q = deque()
    q.append(i)
    check[i] = True
    while q:
        x = q.popleft()
        for next in a[x]:
            if ans[next] == -1:
                ans[next] = ans[x] + 1
                q.append(next)

for i in range(n):
    check = [False] * n
    if cycle(i,i,0,[i]):
        break

check = [False] * n
for i in range(n):
    if ans[i] == 0:
        bfs(i)
print(*ans)