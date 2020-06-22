#https://www.acmicpc.net/problem/12865

import sys

n, k = map(int,sys.stdin.readline().split())
item = [(0,0)]
d = [[0] * (k+1) for _ in range(n+1)]

for _ in range(n):
    w,v = map(int,sys.stdin.readline().split())
    item.append((w,v))
item.sort(key = lambda x : (x[0],x[1]))

if item[1][0] <= k:
    for i in range(item[1][0],k+1):
        d[1][i] = item[1][1]

for i in range(2,n+1):
    for j in range(1,k+1):
        d[i][j] = d[i-1][j] # i 선택 x
        if j - item[i][0] >= 0:  # i 선택 o
            d[i][j] = max(d[i-1][j-item[i][0]] + item[i][1],d[i][j])
print(d[n][k])