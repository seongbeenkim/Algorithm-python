#https://www.acmicpc.net/problem/13023

import sys

n, m = map(int,sys.stdin.readline().split())
visited = [False] * n
a = [[] for _ in range(n)]

for _ in range(m):
    u,v = map(int,sys.stdin.readline().split())
    a[u].append(v)
    a[v].append(u)


def dfs(index,depth,candi):
    visited[index] = True
    if depth == 4:
        return True

    for next in a[index]:
        if not visited[next]:
            if dfs(next,depth+1,candi+[next]):
               return True
            visited[next] = False

    return False

ans = False
for i in range(n):
    if dfs(i,0,[i]):
        ans = True
        break
    visited[i] = False
print(1 if ans else 0)