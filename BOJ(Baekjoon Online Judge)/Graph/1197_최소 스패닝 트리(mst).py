#https://www.acmicpc.net/problem/1197

import sys

v, e = map(int,sys.stdin.readline().split())
a = []
parent = [0] * (v+1)
rank = [1] * (v+1)

def union(u,v):
    x = find(u)
    y = find(v)
    if x == y:
        return
    if rank[x] < rank[y]:
        x,y = y,x
    parent[y] = x
    if rank[x] == rank[y]:
        rank[x] += 1

def find(x):
    if parent[x] == x:
        return x
    y = find(parent[x])
    parent[x] = y
    return y

for i in range(v+1):
    parent[i] = i

for _ in range(e):
    start, end, cost = map(int,sys.stdin.readline().split())
    a.append((start,end,cost))
a.sort(key = lambda x : x[2])
ans = 0
for e in a:
    x = find(e[0])
    y = find(e[1])
    if x != y:
        union(x,y)
        ans += e[2]
print(ans)