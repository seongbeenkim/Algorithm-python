#https://www.acmicpc.net/problem/1753

import sys, heapq

v, e = map(int,sys.stdin.readline().split())
start = int(sys.stdin.readline())
a = [[] for _ in range(v+1)]
MAX = 10**9
d = [MAX] * (v+1)
check = [False] * (v+1)

for i in range(e):
    u,v,w = map(int,sys.stdin.readline().split())
    a[u].append((w,v))

q = []
heapq.heappush(q,(0,start))
d[start] = 0

while q:
    c1, now = heapq.heappop(q)
    if d[now] < c1:
        continue
    if check[now] == False:
        check[now] = True
        for c2, next in a[now]:
            if d[next] > d[now] + c2:
                d[next] = d[now] + c2
                heapq.heappush(q,(d[next],next))
print(check,d)
for x in d[1:]:
    if x == MAX:
        print("INT", end= " ")
    else:
        print(x)