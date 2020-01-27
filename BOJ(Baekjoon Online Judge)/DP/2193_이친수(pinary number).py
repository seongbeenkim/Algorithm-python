#https://www.acmicpc.net/problem/2193

import sys

max = 91
d = [[0]*2 for i in range(max)]
d[1][1] = 1

for i in range(2,max):
    for j in range(2):
        if j == 0:
            d[i][j] = d[i-1][j] + d[i-1][j+1]
        else:
            d[i][j] = d[i-1][j-1]
n = int(sys.stdin.readline())
print(sum(d[n]))