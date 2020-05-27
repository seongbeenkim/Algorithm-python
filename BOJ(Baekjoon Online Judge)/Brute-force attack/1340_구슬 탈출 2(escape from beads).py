#https://www.acmicpc.net/problem/13460

import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())
a = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
rx,ry,bx,by = 0,0,0,0
q = deque()

for i in range(n):
    for j in range(m):
        if a[i][j] == "R":
            rx,ry = i,j
        elif a[i][j] == "B":
            bx,by = i,j

q.append((rx,ry,bx,by,1))
visited[rx][ry][bx][by] = True

def move(x,y,dx,dy):
    cnt = 0
    while a[x+dx][y+dy] != "#" and a[x][y] != "O":
        x += dx
        y += dy
        cnt += 1
    return x,y,cnt

def bfs():
    while q:
        rx, ry, bx, by, depth = q.popleft()

        if depth > 10:
            break

        for k in range(4):
            nrx,nry,rcnt = move(rx,ry,dx[k],dy[k])
            nbx,nby,bcnt = move(bx,by,dx[k],dy[k])

            if a[nbx][nby] != "O":
                if a[nrx][nry] == "O":
                    print(depth)
                    return

                if nrx == nbx and nry == nby:
                    if rcnt > bcnt:
                        nrx -= dx[k]
                        nry -= dy[k]
                    else:
                        nbx -= dx[k]
                        nby -= dy[k]

                if not visited[nrx][nry][nbx][nby]:
                    visited[nrx][nry][nbx][nby] = True
                    q.append((nrx,nry,nbx,nby,depth+1))

    print(-1)

bfs()
