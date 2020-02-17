#https://www.acmicpc.net/problem/2667

import sys,queue

sys.setrecursionlimit(10*6)

n = int(sys.stdin.readline())
a = [list(map(int,list(sys.stdin.readline().strip()))) for _ in range(n)]
check = [[False] * n for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

group = []

def dfs(x,y,c):
    check[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            if a[nx][ny] == 1 and check[nx][ny] == False:
                c = dfs(nx,ny,c+1)
    return c

def bfs(x,y,c):
    q = queue.Queue()
    q.put((x,y))
    check[x][y] = True
    while not q.empty():
        x, y = q.get()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                if a[nx][ny] == 1 and check[nx][ny] == False:
                    check[nx][ny] = True
                    q.put((nx,ny))
                    c += 1
    return c

for i in range(n):
    for j in range(n):
        if a[i][j] == 1 and check[i][j] == False:
            group.append(bfs(i,j,1)) #dfs(i,j,1)

print(len(group))
group.sort()
for i in group:
    print(i)