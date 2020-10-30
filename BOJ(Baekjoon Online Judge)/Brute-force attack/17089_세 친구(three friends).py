#https://www.acmicpc.net/problem/17089

import sys

n, m = map(int,sys.stdin.readline().split())
relationship = [[False] * (n + 1) for _ in range(n + 1)]
degree = [0] * (n+1)
MIN = 2147383647
answer = MIN

for _ in range(m):
    a, b = map(int,sys.stdin.readline().split())
    relationship[a][b] = True
    relationship[b][a] = True
    degree[a] += 1
    degree[b] += 1

for i in range(1,n+1):
    for j in range(i+1,n+1):
        if relationship[i][j]:
            for k in range(j+1,n+1):
                if relationship[i][k] and relationship[j][k]:
                    answer = min(answer,degree[i] + degree[j] + degree[k] - 6)

if answer == MIN:
    answer = -1
print(answer)