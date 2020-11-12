#https://www.acmicpc.net/problem/16988

import sys
from collections import deque

n, m = map(int,sys.stdin.readline().split())
a = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
answer = 0
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs():
    total_count = 0
    check = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if a[i][j] != 2 or check[i][j]:
                continue
            cnt = 1
            q = deque()
            q.append((i,j))
            check[i][j] = True
            is_zero = False
            while q:
                x, y = q.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < n and 0 <= ny < m:
                        if a[nx][ny] == 0:
                            is_zero = True
                        elif a[nx][ny] == 2 and not check[nx][ny]:
                            cnt += 1
                            check[nx][ny] = True
                            q.append((nx,ny))

            if not is_zero:
                total_count += cnt
    return total_count

for x1 in range(n):
    for y1 in range(m):
        if a[x1][y1] != 0:
            continue
        a[x1][y1] = 1

        for x2 in range(n):
            for y2 in range(m):
                if a[x2][y2] != 0:
                    continue
                a[x2][y2] = 1
                res = bfs()
                answer = max(res,answer)
                a[x2][y2] = 0

        a[x1][y1] = 0
print(answer)