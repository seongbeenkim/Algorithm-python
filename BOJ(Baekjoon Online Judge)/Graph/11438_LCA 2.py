#https://www.acmicpc.net/problem/11438

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

q = deque()
q.append(1)
check[1] = True

while q:
    x = q.popleft()

    for y in a[x]:
        if not check[y]:
            check[y] = True
            d[y] = d[x] + 1
            parent[y] = x
            q.append(y)

log = 1
while (1<<log) <= n:
    log += 1

p = [[0] * log for _ in range(n+1)]

for i in range(1,n+1):
    p[i][0] = parent[i]

j = 1

while (1<<j) < n:
    for i in range(1,n+1):
        if p[i][j-1] != 0:
            p[i][j] = p[p[i][j-1]][j-1]

    j+=1


def lca(x,y):

    if d[x] < d[y]:
        x, y = y, x

    log = 1

    while (1<<log) <= d[x]:
        log += 1

    for i in range(log,-1,-1):
        if d[x] - (1<<i) >= d[y]:
            x = p[x][i]
    if x == y:
        return x
    else:
        for i in range(log, -1, -1):
            if p[x][i] != 0 and p[x][i] != p[y][i]:
                x = p[x][i]
                y = p[y][i]

    return parent[x]
m = int(sys.stdin.readline())
for _ in range(m):
    s, e = map(int,sys.stdin.readline().split())
    print(lca(s,e))