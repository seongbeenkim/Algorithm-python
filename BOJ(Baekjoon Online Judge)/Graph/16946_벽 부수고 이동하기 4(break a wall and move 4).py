#https://www.acmicpc.net/problem/16946

import sys
from collections import deque

n, m = map(int,sys.stdin.readline().split())
a = [list(map(int,sys.stdin.readline().rstrip())) for _ in range(n)]
group = [[-1] * m for _ in range(n)]
check = [[False] * m for _ in range(n)]
group_size = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(i,j):
    g = len(group_size)
    cnt = 1
    d = deque()
    d.append((i,j))
    check[i][j] = True
    group[i][j] = g

    while d:
        x, y = d.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not check[nx][ny] and a[nx][ny] == 0:
                    d.append((nx,ny))
                    group[nx][ny] = g
                    check[nx][ny] = True
                    cnt += 1

    group_size.append(cnt)

for i in range(n):
    for j in range(m):
        if a[i][j] == 0 and not check[i][j]:
            bfs(i,j)

for i in range(n):
    for j in range(m):
        if a[i][j] == 1:
            same = set()
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < n and 0 <= ny < m:
                    if a[nx][ny] == 0:
                        same.add(group[nx][ny])
            cnt = 1
            for g in same:
                cnt += group_size[g]
            print(cnt % 10, end="")
        else:
            print(0,end="")
    print()