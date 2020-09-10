#https://www.acmicpc.net/problem/1389

import sys

n, m = map(int,sys.stdin.readline().split())

INF = 2147383647
a = [[INF] * (n+1) for _ in range(n+1)]

for _ in range(m):
    x, y = map(int,sys.stdin.readline().split())
    a[x][y] = 1
    a[y][x] = 1

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if a[i][k] != INF and a[k][j] != INF and i!=j:
                if a[i][j] > a[i][k] + a[k][j]:
                    a[i][j] = a[i][k] + a[k][j]
ans = [INF]
for i in range(1,n+1):
    total = 0
    for j in range(1,n+1):
        if i != j:
            total += a[i][j]
    ans.append(total)

print(ans.index(min(ans)))