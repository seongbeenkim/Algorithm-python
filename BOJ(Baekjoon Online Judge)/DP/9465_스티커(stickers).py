#https://www.acmicpc.net/problem/9465

import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    a = [list(map(int,sys.stdin.readline().split())) for _ in range(2)]
    d = [[0] * 3 for _ in range(n)]
    for i in range(n):
        d[i][0] = max(d[i-1])
        d[i][1] = max(d[i-1][0],d[i-1][2]) + a[0][i]
        d[i][2] = max(d[i-1][0],d[i-1][1]) + a[1][i]
    ans = max(d[n-1])
    print(ans)
"""
    d = [[0] * n for _ in range(2)]
    d[0][0] = a[0][0]
    d[1][0] = a[1][0]
    d[0][1] = a[0][1] + a[1][0]
    d[1][1] = a[1][1] + a[0][0]

    for i in range(2,n):
        d[0][i] = max(d[1][i-1] + a[0][i],d[1][i-2] + a[0][i])
        d[1][i] = max(d[0][i-1] + a[1][i],d[0][i-2] + a[1][i])
    print(max(d[0][n-1],d[1][n-1]))
"""