#https://www.acmicpc.net/problem/1916

import sys, heapq

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
a = [[] for _ in range(n+1)]
v = [0] * (n+1)
check = [False] * (n+1)
MAX = 10**9
d = [MAX] * (n+1)

for i in range(m):
    s,e,c = map(int,sys.stdin.readline().split())
    a[s].append((c,e))
start, end = map(int,sys.stdin.readline().split())

q = []
heapq.heappush(q,(0,start))
d[start] = 0
v[start] = -1
while q:
    c1,e1 = heapq.heappop(q)
    if d[e1] < c1:
        continue
    if check[e1] == False:
        for c2,e2 in a[e1]:
            if d[e1] != MAX and d[e2] > d[e1] + c2:
                d[e2] = d[e1] + c2
                v[e2] = e1
                check[e1] = True
                heapq.heappush(q,(d[e2],e2))

print(d[end])
x = end
stack = []
while x != -1:
    stack.append(x)
    x = v[x]
print(len(stack))
print(*stack[::-1])