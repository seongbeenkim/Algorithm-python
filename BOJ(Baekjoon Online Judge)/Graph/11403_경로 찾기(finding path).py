#https://www.acmicpc.net/problem/11403

import sys
from collections import deque

n = int(sys.stdin.readline())
d = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if d[i][k] != 0 and d[k][j] != 0: #if d[i][k] + d[k][j] == 2:
                d[i][j] = 1
for i in range(n):
    print(*d[i])
