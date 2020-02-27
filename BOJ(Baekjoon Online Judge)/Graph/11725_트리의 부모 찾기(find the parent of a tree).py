#https://www.acmicpc.net/problem/11725

import sys
from collections import deque
sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline())
d = [[] for _ in range(n+1)]
parent = [0] * (n+1)
check = [False] * (n+1)
depth = [1] * (n+1)
q = deque()

for _ in range(n-1):
    u, v = map(int,sys.stdin.readline().split())
    d[u].append(v)
    d[v].append(u)
def bfs(start):
    q.append(start)
    check[start] = True
    while q:
        x = q.popleft()
        for i in d[x]:
            if check[i] == False:
                q.append(i)
                check[i] = True
                depth[i] = depth[x] + 1; parent[i] = x
def dfs(start):
    check[start] = True
    for i in d[start]:
        if check[i] == False:
            check[i] = True
            depth[i] = depth[start] + 1
            parent[i] = start
            dfs(i)
bfs(1) # dfs(1)
for i in range(2,n+1):
    print(parent[i])