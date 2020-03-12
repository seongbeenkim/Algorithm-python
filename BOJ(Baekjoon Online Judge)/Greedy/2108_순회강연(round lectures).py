#https://www.acmicpc.net/problem/2109

import sys, heapq

n = int(sys.stdin.readline())
MIN = 0
lectures = []

for i in range(n):
    p, d = map(int,sys.stdin.readline().split())
    lectures.append((p,d))

lectures.sort(key = lambda x : (x[1],x[0]),reverse=True)

sum = 0
k = 0
h = []
for i in range(10000,0,-1):
    while k < n and lectures[k][1] == i:
        heapq.heappush(h,-lectures[k][0])
        k += 1
    if h:
        sum += -heapq.heappop(h)
print(sum)