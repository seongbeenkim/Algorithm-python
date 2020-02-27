#https://www.acmicpc.net/problem/1167

import sys
from collections import deque

sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())
connection = [set([]) for _ in range(n+1)]
check = [False] * (n+1)

for _ in range(n):
    a = list(map(int,sys.stdin.readline().split()))[:-1]
    for i in range(1,len(a)):
        if i%2 == 0: # 1 => vertex, 0 => dist
            connection[a[0]].add((a[i-1],a[i])) # (vertex,dist)
            connection[a[i-1]].add((a[0],a[i])) # (vertex,dist)

def dfs(v):
    check[v] = True
    for i in connection[v]:
        v2,d2 = i
        if check[v2] == False:
            dist[v2] = dist[v] + d2
            check[v2] = True
            dfs(v2)

def bfs(start):
    dist = [0] * (n + 1)
    check = [False] * (n + 1)
    q = deque()
    q.append(start)
    check[start] = True
    while q:
        x = q.popleft()

        for i in connection[x]:
            v, d = i
            if check[v] == False:
                check[v] = True
                dist[v] = dist[x] + d
                q.append(v)

    return dist

dist = [0] * (n + 1)
check = [False] * (n + 1)
dfs(1)

start = 1
for i in range(2,n+1):
    if dist[i] > dist[start]:
        start = i
dist = [0] * (n + 1)
check = [False] * (n + 1)
dfs(start)
print(max(dist))

### bfs
"""
dist = bfs(1)
start = 1
for i in range(2,n+1):
    if dist[i] > dist[start]:
        start = i
dist = bfs(start)
print(max(dist))
"""