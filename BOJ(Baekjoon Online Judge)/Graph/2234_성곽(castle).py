#https://www.acmicpc.net/problem/2234

import sys
from collections import deque

m, n = map(int,sys.stdin.readline().split())
a = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

d = [[-1] * m for _ in range(n)]
group_size = []
group_number = -1

dx = [0,-1,0,1] # 서북동남
dy = [-1,0,1,0]

def bfs(i,j):
    global group_number
    q = deque()
    q.append((i,j))
    group_number += 1
    d[i][j] = group_number
    cnt = 1

    while q:
        x, y = q.popleft()
        number = a[x][y]   # 1111 남동북서
        dir = []
        for i in range(4):
            if number & (1 << i):
                continue
            else:
                dir.append(i)

        if dir:
            for k in dir:
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < n and 0 <= ny < m and d[nx][ny] == -1:
                    d[nx][ny] = group_number
                    q.append((nx,ny))
                    cnt += 1

    group_size.append(cnt)

for i in range(n):
    for j in range(m):
        if d[i][j] == -1:
            bfs(i,j)

answer = max(group_size)
for i in range(n):
    for j in range(m):
        number = a[i][j]
        dir = []
        for l in range(4):
            if number & (1 << l):
                dir.append(l)
        if dir:
            for k in dir:
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < n and 0 <= ny < m and d[nx][ny] != d[i][j]:
                    answer = max(answer, group_size[d[nx][ny]] + group_size[d[i][j]])
"""
for i in range(n):
    for j in range(m):
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < n and 0 <= ny < m and d[nx][ny] != d[i][j]:
                answer = max(answer, group_size[d[nx][ny]] + group_size[d[i][j]])
"""

print(group_number+1)
print(max(group_size))
print(answer)
