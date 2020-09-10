#https://www.acmicpc.net/problem/1916

import sys, heapq

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
a = [[] for _ in range(n+1)]
INF = 100000001
dist = [INF] * (n+1)
check = [False] * (n+1)

for i in range(m):
    s, e, c = map(int,sys.stdin.readline().split())
    a[s].append([e,c])
start, end = map(int,sys.stdin.readline().split())

dist[start] = 0
q = []
heapq.heappush(q,[0,start])
while q:
    c, s = heapq.heappop(q)
    if dist[s] < c:
        continue
    if check[s] == False:
        for e, t in a[s]:
            if dist[s] != INF and dist[e] > dist[s] + t:
                dist[e] = dist[s] + t
                heapq.heappush(q,[dist[e],e])
                check[s] = True
print(dist[end])

"""
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

a = [[] for _ in range(n+1)]
d = [214738364] * (n+1)

for _ in range(m):
    x, y, c = map(int,sys.stdin.readline().split())
    a[x].append((c,y))

start, end = map(int,sys.stdin.readline().split())

h = []
d[start] = 0
heapq.heappush(h,(0,start))

while h:
    c, x = heapq.heappop(h)
    for cost, y in a[x]:
        if d[y] > d[x] + cost:
            d[y] = d[x] + cost
            heapq.heappush(h,(d[y],y))

print(d[end])
"""