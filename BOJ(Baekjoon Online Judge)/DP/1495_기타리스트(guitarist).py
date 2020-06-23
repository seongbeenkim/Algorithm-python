#https://www.acmicpc.net/problem/1495

import sys

n,s,m = map(int,sys.stdin.readline().split())
v = [0] + list(map(int,sys.stdin.readline().split()))
d = [[-1] * (m+1) for _ in range(n+1)]
d[0][s] = s

for i in range(1,n+1):
    for j in range(m+1):
        if d[i-1][j] != -1:
            if j-v[i] >= 0:
                d[i][j-v[i]] = j-v[i]
            if j+v[i] <= m:
                d[i][j+v[i]] = j+v[i]
print(max(d[n]))

"""
d = [[0] * (m+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(m+1):
        if d[i-1][j] == 1:
            if j-v[i] >= 0:
                d[i][j-v[i]] = 1
            if j+v[i] <= m:
                d[i][j+v[i]] = 1
ans = -1
for i in range(m+1):
    if d[n][i]:
        ans = i
print(ans)
"""