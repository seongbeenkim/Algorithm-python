#https://www.acmicpc.net/problem/16932

import sys
from collections import deque

n, m = map(int,sys.stdin.readline().split())
a = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
MIN = 0
answer = MIN

dx = [0,0,1,-1]
dy = [1,-1,0,0]

group = [[0] * m for _ in range(n)]
group_number = 0
group_size = [0]

def bfs(i,j):
    global group_number
    group_number += 1
    q = deque()
    q.append((i,j))
    group[i][j] = group_number
    cnt = 1
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and group[nx][ny] == 0 and a[nx][ny] == 1:
                group[nx][ny] = group_number
                q.append((nx,ny))
                cnt += 1
        
    group_size.append(cnt)

for i in range(n):
    for j in range(m):
        if a[i][j] == 1 and group[i][j] == 0:
            bfs(i,j)

for i in range(n):
    for j in range(m):
        if a[i][j] == 0:
            d = set()
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < n and 0 <= ny < m and a[nx][ny] == 1:
                    d.add(group[nx][ny])
            total = 1
            for near in d:
                total += group_size[near]
            answer = max(total,answer)

print(answer)