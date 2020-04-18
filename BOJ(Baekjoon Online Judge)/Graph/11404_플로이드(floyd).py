#https://www.acmicpc.net/problem/11404

import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
INF = 10**9
a = [[INF] * (n+1) for _ in range(n+1)]

for i in range(n+1):
    a[i][i] = 0

for _ in range(m):
    s, e, c = map(int,sys.stdin.readline().split())
    if a[s][e] > c:
        a[s][e] = c

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i!=j and a[i][j] > a[i][k] + a[k][j]:
                a[i][j] = a[i][k] + a[k][j]

for i in range(1,n+1):
    for j in range(1,n+1):
        if a[i][j] == INF:
            a[i][j] = 0
        print(a[i][j], end =" ")
    print()