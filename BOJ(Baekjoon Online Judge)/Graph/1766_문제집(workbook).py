#https://www.acmicpc.net/problem/1766

import sys, heapq

n, m = map(int,sys.stdin.readline().split())
a = [[] for _ in range(n+1)]
val = [0] * (n+1)
for _ in range(m):
    A, B = map(int,sys.stdin.readline().split())
    a[A].append(B)
    val[B] += 1

heap = []

for i in range(1,n+1):
    if val[i] == 0:
        heapq.heappush(heap, i)
while heap:
    x = heapq.heappop(heap)
    print(x, end=" ")
    for i in a[x]:
        val[i] -= 1
        if val[i] == 0:
            heapq.heappush(heap,i)