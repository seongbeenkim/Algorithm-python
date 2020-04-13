#https://www.acmicpc.net/problem/1922

import sys, heapq

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

a = [[] for _ in range(n+1)]
dist = [[0] * (n+1) for _ in range(n+1)]
check = [False] * (n+1)
heap = []
ans = 0
for _ in range(m):
    start, end, cost = map(int,sys.stdin.readline().split())
    a[start].append((cost,end))
    a[end].append((cost,start))

check[1] = True
for i in a[1]:
    heapq.heappush(heap, i)

while heap:
    cost, v = heapq.heappop(heap)
    if check[v] == True:
        continue
    check[v] = True
    ans += cost
    for i in a[v]:
        if check[i[1]] == False:
            heapq.heappush(heap,i)
print(ans)
