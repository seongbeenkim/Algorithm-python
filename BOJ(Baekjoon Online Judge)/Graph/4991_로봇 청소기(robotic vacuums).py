#https://www.acmicpc.net/problem/4991

import sys
from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def next_permutation(a):
    i = len(a) - 1

    while i > 0 and a[i - 1] >= a[i]:
        i -= 1

    if i <= 0:
        return False

    j = len(a) - 1

    while a[j] <= a[i - 1]:
        j -= 1

    a[i - 1], a[j] = a[j], a[i - 1]

    j = len(a) - 1

    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1

    return True


def bfs(a, i, j):
    d = [[-1] * m for _ in range(n)]
    q = deque()
    q.append((i, j))
    d[i][j] = 0

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and a[nx][ny] != 'x':
                if d[nx][ny] == -1:
                    d[nx][ny] = d[x][y] + 1
                    q.append((nx, ny))

    return d

while True:
    m, n = map(int,sys.stdin.readline().split())
    if n == 0 and m == 0:
        break

    a = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
    dust = [(0,0)]

    for i in range(n):
        for j in range(m):
            if a[i][j] == 'o':
                dust[0] = (i,j)

            elif a[i][j] == '*':
                dust.append((i,j))

    l = len(dust)

    d = [[-1] * l for _ in range(l)]

    is_possible = True
    
    for i in range(l):
        dist = bfs(a, dust[i][0], dust[i][1])
        for j in range(l):
            d[i][j] = dist[dust[j][0]][dust[j][1]]
            if d[i][j] == -1:
                is_possible = False

    if not is_possible:
        print(-1)
        continue

    answer = 400
    p = [i+1 for i in range(l-1)] # l-1 해주는 이유는 청소기의 위치를 빼주기 위해서이며 i+1도 마찬가지다.

    while True:
        res = d[0][p[0]]
        for i in range(len(p)-1):
            res += d[p[i]][p[i+1]]
        answer = min(answer,res)
        if not next_permutation(p):
            break
    print(answer)