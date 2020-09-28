#https://www.acmicpc.net/problem/10026

import sys
from collections import deque

n = int(sys.stdin.readline())

a = [sys.stdin.readline().rstrip() for _ in range(n)]
p1 = []
p2 = []
c1 = [[False]*n for _ in range(n)]
c2 = [[False]*n for _ in range(n)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
ans1 = 0
ans2 = 0

def bfs(i,j,person):
    q = deque()
    q.append((i,j,person))
    if person == 1:
        c1[i][j] = True
    else:
        c2[i][j] = True

    while q:
        x, y, p = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if p == 1:
                    if a[x][y] == a[nx][ny] and not c1[nx][ny]:
                        c1[nx][ny] = True
                        q.append((nx,ny,p))
                else:
                    if a[x][y] == 'R' or a[x][y] == 'G':
                        if a[nx][ny] != 'B' and not c2[nx][ny]:
                            c2[nx][ny] = True
                            q.append((nx,ny,p))
                    else:
                        if a[x][y] == a[nx][ny] and not c2[nx][ny]:
                            c2[nx][ny] = True
                            q.append((nx,ny,p))

for i in range(n):
    for j in range(n):
        if not c1[i][j]:
            bfs(i,j,1)
            ans1 += 1

        if not c2[i][j]:
            bfs(i,j,2)
            ans2 += 1

print(ans1, ans2)