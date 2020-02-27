#https://www.acmicpc.net/problem/11725

import sys
from collections import deque

n = int(sys.stdin.readline())
d = [[] for _ in range(n+1)]
parent = [0] * (n+1)
check = [False] * (n+1)
depth = [0] * (n+1)
q = deque()

for _ in range(n-1):
    u, v = map(int,sys.stdin.readline().split())
    d[u].append(v)
    d[v].append(u)

q.append(1)
check[1] = True
depth[1] = 1
while q:
    x = q.popleft()
    for i in d[x]:
        if check[i] == False:
            q.append(i)
            check[i] = True
            depth[i] = depth[x] + 1
            parent[i] = x
for i in range(2,n+1):
    print(parent[i])