#https://www.acmicpc.net/problem/11437

import sys
from collections import deque

n = int(sys.stdin.readline())
a = [[] for _ in range(n+1)]
d = [0] * (n+1)
parent = [0] * (n+1)
check = [False] * (n+1)

for _ in range(n-1):
    s, e = map(int,sys.stdin.readline().split())
    a[s].append(e)
    a[e].append(s)

start = 1
q = deque()
q.append(start)
check[start] = True
d[start] = 0
parent[start] = 0

while q:
    x = q.popleft()
    for y in a[x]:
        if check[y] == False:
            check[y] = True
            d[y] = d[x] + 1
            parent[y] = x
            q.append(y)

#dfs
"""
def set_level(i):
    check[i] = True

    if len(a[i]) == 0:
        return

    for j in a[i]:
        if not check[j]:
            d[j] = d[i] + 1
            parent[j] = i
            set_level(j)

set_level(1)
"""
def lca(x,y):
    if d[x] < d[y]:
        x, y = y, x
    while d[x] != d[y]:
        x = parent[x]
    while x != y:
        x = parent[x]
        y = parent[y]
    return x

m = int(sys.stdin.readline())
for _ in range(m):
    x, y = map(int,sys.stdin.readline().split())
    print(lca(x,y))