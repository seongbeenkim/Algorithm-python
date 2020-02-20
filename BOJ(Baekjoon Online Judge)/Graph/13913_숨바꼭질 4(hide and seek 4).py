#https://www.acmicpc.net/problem/13913

import sys
from collections import deque

sys.setrecursionlimit(10**6)

MAX = 200000
n, k = map(int,sys.stdin.readline().split())
check = [False] * (MAX + 1)
d = [-1] * (MAX + 1)
v = [0] * (MAX + 1)

def bfs(i):
    q = deque()
    check[i] = True
    d[i] = 0
    q.append(i)
    while q :
        x = q.popleft()
        for next in [x-1, x+1, x*2]:
            if 0 <= next <= MAX and check[next] == False:
                q.append(next)
                check[next] = True
                d[next] = d[x] + 1
                v[next] = x

bfs(n)
print(d[k])

ans = []
while n != k:
    ans.append(k)
    k = v[k]
ans.append(k)
ans.reverse()
print(" ".join(map(str,ans)))
"""
def go(n,k):
    if n != k:
        go(n,v[k])
    print(k, end = " ")
go(n,k)
"""