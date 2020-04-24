#https://www.acmicpc.net/problem/11657

import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())
a = [[] for _ in range(n+1)]
maximum = 10000001
dist = [maximum] * (n+1)

for i in range(m):
    s, e, c = map(int,sys.stdin.readline().split())
    a[s].append((e,c))

dist[1] = 0
check = [False] *(n+1)
check[1] = True
q = deque()
q.append(1)

while q:
    x = q.popleft()
    check[x] = False
    for e,c in a[x]:
        if dist[e] > dist[x] + c:
            dist[e] = dist[x] + c
            if check[e] == False:
                q.append(e)
                check[e] = True

for i in range(2,n+1):
    if dist[i] == maximum:
        print(-1)
    else:
        print(dist[i])
# Bellman-Ford
"""
n,m = map(int,sys.stdin.readline().split())
a = []
maximum = 10000001
dist = [maximum] * (n+1)

for _ in range(m):
    start,end,cost = map(int,sys.stdin.readline().split())
    a.append((start,end,cost))

dist[1] = 0
negative = False
for i in range(1,n+1):
    for start, end, cost in a:
        if dist[start] != maximum and dist[end] > dist[start] + cost:
            dist[end] = dist[start] + cost
            if i == n:
                negative = True

if negative:
    print(-1)
else:
    for i in dist[2:]:
        if i == maximum:
            print(-1)
        else:
            print(i)
"""