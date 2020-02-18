from collections import deque
dx = [0,0,1,-1,1,1,-1,-1]
dy = [1,-1,0,0,1,-1,1,-1]
def bfs(x, y, cnt):
    q = deque()
    q.append((x,y))
    group[x][y] = cnt
    while q:
        x, y = q.popleft()
        for k in range(8):
            nx, ny = x+dx[k], y+dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if a[nx][ny] == 1 and group[nx][ny] == 0:
                    q.append((nx,ny))
                    group[nx][ny] = cnt
while True:
    m,n = map(int,input().split())
    if n == 0 and m == 0:
        break
    a = [list(map(int,input().split())) for _ in range(n)]
    group = [[0]*m for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if a[i][j] == 1 and group[i][j] == 0:
                cnt += 1
                bfs(i, j, cnt)

    print(cnt)
