#https://www.acmicpc.net/problem/1707

import sys
from collections import deque

sys.setrecursionlimit(10**6)
def dfs(x,c):
    check[x] = c
    for i in a[x]:
        if check[i] == 0:
            if not dfs(i,3-c):
                return False
        elif check[i] == check[x]:
            return False
    return True

def bfs(x,c):
    q = deque()
    q.append(x)
    check[x] = c
    while q:
        x = q.popleft()
        c = check[x]
        for i in a[x]:
            if check[i] == 0:
                check[i] = 3-c
                q.append(i)
            elif check[i] == check[x]:
                return False
    return True

t = int(sys.stdin.readline())

for i in range(t):
    n, m = map(int,sys.stdin.readline().split())
    a = [[] for _ in range(n+1)]
    check = [0] * (n+1)
    for i in range(m):
        u, v = map(int,sys.stdin.readline().split())
        a[u].append(v)
        a[v].append(u)
    for i in range(1,n+1):
        a[i].sort()
    ans = True

    for i in range(1,n+1):
        if check[i] == 0 and ans == True:
            if not bfs(i,1): #dfs(i,1)
                ans = False
    sys.stdout.write(('YES' if ans else 'NO')+ "\n")