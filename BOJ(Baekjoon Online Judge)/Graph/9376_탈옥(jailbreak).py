#https://www.acmicpc.net/problem/9376

import sys
from collections import deque

t = int(sys.stdin.readline())

for _ in range(t):
    n, m = map(int,sys.stdin.readline().split())
    a = [['.'] + list(sys.stdin.readline().rstrip()) + ['.'] for _ in range(n)]
    a.insert(0,['.']*(m+2))
    a.append(['.']*(m+2))

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    def bfs(i,j):

        d = [[-1] * (m+2) for _ in range(n+2)]
        d[i][j] = 0
        q = deque()
        q.append((i,j))

        while q:
            x,y = q.popleft()
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < n+2 and 0 <= ny < m+2 and d[nx][ny] == -1 and a[nx][ny] != '*':
                    if a[nx][ny] == '#':
                        d[nx][ny] = d[x][y] + 1
                        q.append((nx,ny))

                    else:
                        d[nx][ny] = d[x][y]
                        q.appendleft((nx,ny))
        return d

    prisoner = []
    for i in range(n + 2):
        for j in range(m + 2):
            if a[i][j] == '$':
                prisoner.append((i, j))
    answer = 100 * 100
    d0 = bfs(0, 0)
    d1 = bfs(prisoner[0][0],prisoner[0][1])
    d2 = bfs(prisoner[1][0],prisoner[1][1])

    for i in range(n + 2):
        for j in range(m + 2):
            if a[i][j] == '*':
                continue
            k = d0[i][j]+d1[i][j]+d2[i][j]
            if a[i][j] == '#':
                k -= 2
            answer = min(answer, k)
    print(answer)