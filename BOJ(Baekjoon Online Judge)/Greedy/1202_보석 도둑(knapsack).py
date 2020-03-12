#https://www.acmicpc.net/problem/1202

import heapq, sys

n, k = map(int,sys.stdin.readline().split())
h = []
total = []
MAX = 1000001
for i in range(n):
    m,v = list(map(int,sys.stdin.readline().split()))
    total.append((m,v))
for i in range(k):
    k = int(sys.stdin.readline())
    total.append((k,MAX))
total.sort()

sum = 0
for i in total:
    if i[1] == MAX:
        if h:
            sum += heapq.heappop(h)[0]
    else:
        heapq.heappush(h,(-i[1],i[0]))
print(-sum)