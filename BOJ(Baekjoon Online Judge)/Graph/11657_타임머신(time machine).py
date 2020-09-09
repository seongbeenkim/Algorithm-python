#https://www.acmicpc.net/problem/11657

import sys

# Bellman-Ford

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
