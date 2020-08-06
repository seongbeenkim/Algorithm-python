#https://www.acmicpc.net/problem/7562

import sys
from collections import deque

t = int(sys.stdin.readline())
dx = [-2,-2,-1,1,2,2,1,-1]
dy = [-1,1,2,2,1,-1,-2,-2]

for _ in range(t):
    n = int(sys.stdin.readline())
    start = tuple(map(int,sys.stdin.readline().split()))
    end = tuple(map(int,sys.stdin.readline().split()))

    d = [[-1] * n for _ in range(n)]

    q = deque()
    q.append(start)
    d[start[0]][start[1]] = 0

    while q:
        x, y = q.popleft()
        if x == end[0] and y == end[0]:
            break
        for k in range(8):
            nx = dx[k] + x
            ny = dy[k] + y
            if 0 <= nx < n and 0 <= ny < n and d[nx][ny] == -1:
                d[nx][ny] = d[x][y] + 1
                q.append((nx,ny))

    print(d[end[0]][end[1]])

# 이 코드는 Python 3 에서 시간초과, but Pypy3 에서는 통
"""
    while q:
        x, y = q.popleft()
        for k in range(8):
            nx = dx[k] + x
            ny = dy[k] + y
            if 0 <= nx < n and 0 <= ny < n:
                if d[nx][ny] == -1 or d[x][y] + 1 < d[nx][ny]:
                    d[nx][ny] = d[x][y] + 1
                    q.append((nx,ny))
"""