#https://www.acmicpc.net/problem/2210

import sys

n = 5
a = [list(sys.stdin.readline().split()) for _ in range(n)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]
answer = {}

def dfs(x,y,res):
    global answer

    if len(res) == 6:
        if res not in answer:
            answer[res] = 1
        return
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < n:
            dfs(nx,ny,res+a[nx][ny])

for i in range(n):
    for j in range(n):
        dfs(i,j,a[i][j])

print(len(answer))