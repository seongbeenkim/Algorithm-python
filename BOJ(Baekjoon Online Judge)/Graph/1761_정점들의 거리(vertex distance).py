#https://www.acmicpc.net/problem/1761

import sys
from collections import deque

n = int(sys.stdin.readline())
a = [[] for _ in range(n+1)]
check = [False] * (n+1)
dist = [0] * (n+1)
depth = [0] * (n+1)
parent = [0] * (n+1)

for _ in range(n-1):
    u, v, c = map(int,sys.stdin.readline().split())
    a[u].append((c,v))
    a[v].append((c,u))

start = 1
q = deque()
q.append(start)
check[start] = True
parent[start] = 0
depth[start] = 0
dist[start] = 0
while q:
    x = q.popleft()
    for cost, y in a[x]:
        if check[y] == False:
            check[y] = True
            dist[y] = dist[x] + cost
            depth[y] = depth[x] + 1
            parent[y] = x
            q.append(y)

def lca(u,v):
    if depth[u] < depth[v]:
        u, v = v, u
    while depth[u] != depth[v]:
        u = parent[u]
    while u != v:
        u = parent[u]
        v = parent[v]
    return u

m = int(sys.stdin.readline())

for _ in range(m):
    u, v = map(int,sys.stdin.readline().split())
    print(dist[v] + dist[u] - (2*dist[lca(u,v)]))


"""
n = int(sys.stdin.readline())

parent = [0] * (n+1)
d = [0] * (n+1)
dist = [0] * (n+1)
a = [[] for _ in range(n+1)]
check = [False] * (n+1)

for _ in range(n-1):
    s, e, k = map(int,sys.stdin.readline().split())
    a[s].append((e,k))
    a[e].append((s,k))

q = deque()
q.append((1))
check[1] = True

while q:
    x = q.popleft()
    for y, k in a[x]:
        if not check[y]:
            check[y] = True
            d[y] = d[x] + 1
            dist[y] = k
            parent[y] = x
            q.append(y)

def lca(x,y):
    res_x = 0
    res_y = 0

    if d[x] < d[y]:
        x,y = y,x

    while d[x] != d[y]:
        res_x += dist[x]
        x = parent[x]

    while x != y:
        res_x += dist[x]
        res_y += dist[y]
        x = parent[x]
        y = parent[y]

    return res_x + res_y

m = int(sys.stdin.readline())
print(d,dist,parent)
for _ in range(m):
    s, e = map(int,sys.stdin.readline().split())
    print(lca(s,e))
"""