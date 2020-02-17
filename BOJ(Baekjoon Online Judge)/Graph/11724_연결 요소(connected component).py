#https://www.acmicpc.net/problem/11724

import sys, queue
sys.setrecursionlimit(10**6)
n, m = map(int,sys.stdin.readline().split())
a = [[] for _ in range(n+1)]
check = [False] * (n+1)
ans = 0
for i in range(m):
    u,v = map(int,sys.stdin.readline().split())
    a[u].append(v)
    a[v].append(u)

for i in range(1,n+1):
    a[i].sort()

def dfs(x):
    check[x] = True
    for i in a[x]:
        if check[i] == False:
            dfs(i)

def bfs(i):
    cnt = 0
    q = queue.Queue()
    q.put(i)
    check[i] = True
    while not q.empty():
        x = q.get()
        for i in a[x]:
            if check[i] == False:
                check[i] = True
                q.put(i)
for i in range(1,n+1):
    if not check[i]:
        bfs(i) #dfs(i)
        ans += 1
print(ans)