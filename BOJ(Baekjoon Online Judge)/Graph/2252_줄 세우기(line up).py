#https://www.acmicpc.net/problem/2252

import sys
from collections import deque

sys.setrecursionlimit(10**5)

n, m = map(int,sys.stdin.readline().split())
a = [[] for _ in range(n+1)]
val = [0] * (n+1)
q = deque() # for bfs
check = [False] * (n+1) # for dfs
s = []

for _ in range(m):
    x,y = map(int,sys.stdin.readline().split())
    a[y].append(x)

def dfs(x):
    check[x] = True
    for i in a[x]:
        if check[i] == False:
            dfs(i)
    s.append(x)

for i in range(1,n+1):
    if check[i] == False:
        dfs(i)
print(" ".join(map(str,s)))

#bfs
"""
for _ in range(m):
    x,y = map(int,sys.stdin.readline().split())
    a[x].append(y)
    val[y] += 1
    
for i in range(1,n+1):
    if val[i] == 0:
        q.append(i)

while q:
    x = q.popleft()
    print(x, end=" ")
    for k in a[x]:
        val[k] -= 1
        if val[k] == 0:
            q.append(k)
"""