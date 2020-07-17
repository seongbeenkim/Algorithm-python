#https://www.acmicpc.net/problem/17404

import sys

n = int(sys.stdin.readline())
color = [[0,0,0]]
for _ in range(n):
    color.append(list(map(int,sys.stdin.readline().split())))

d = [[0]*3 for _ in range(n+1)]
ans = 2147483647

for k in range(3):
    for j in range(3):
        if k == j:
            d[1][j] = color[1][j]
        else:
            d[1][j] = 2147483647

    for i in range(2,n+1):
        d[i][0] = min(d[i-1][1],d[i-1][2]) + color[i][0]
        d[i][1] = min(d[i-1][0],d[i-1][2]) + color[i][1]
        d[i][2] = min(d[i-1][1],d[i-1][0]) + color[i][2]

    for l in range(3):
        if k == l:
            continue
        ans = min(d[n][l],ans)

print(ans)