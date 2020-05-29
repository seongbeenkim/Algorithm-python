#https://www.acmicpc.net/problem/12100

import sys
from copy import deepcopy

n = int(sys.stdin.readline())
a = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
ans = 0

def move(map,dir):
    can_merged = [[True] * n for _ in range(n)]
    if dir in [0,2]:
        start = 0
        end = n
        step = 1
    else:
        start = n-1
        end = -1
        step = -1

    for i in range(start,end,step):
        for j in range(start,end,step):
            if map[i][j] != 0:
                x,y = i,j

                value = map[i][j]
                map[i][j] = 0

                nx = i+dx[dir]
                ny = j+dy[dir]

                while 0 <= nx < n and 0 <= ny < n:
                    if value == map[nx][ny] and can_merged[nx][ny]:
                        can_merged[nx][ny] = False
                        x,y = nx,ny
                        break

                    elif map[nx][ny] == 0:
                        x = nx
                        y = ny
                        nx += dx[dir]
                        ny += dy[dir]

                    else:
                        break

                map[x][y] = map[x][y] + value

    return map

def count(map):
    global ans
    for i in range(n):
        for j in range(n):
            if map[i][j] != 0:
                ans = max(map[i][j],ans)

def go(map,cnt):
    if cnt == 5:
        count(map)
        return
    for i in range(4):
        copied_map = deepcopy(move(deepcopy(map),i))
        go(copied_map,cnt+1)

go(a,0)
print(ans)