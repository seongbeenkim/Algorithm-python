#https://www.acmicpc.net/problem/16197

import sys

n, m = map(int,sys.stdin.readline().split())
a = [list(sys.stdin.readline()) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

first_coin = []
second_coin = []
check_first = [[False] * m for _ in range(n)]
check_second = [[False] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if a[i][j] == 'o':
            if not first_coin:
                first_coin = [i,j]
            else:
                second_coin = [i,j]

answer = 20*20

def dfs(x1,y1,x2,y2,count):
    global answer
    is_first_drop = False
    is_second_drop = False
    if count > 10:
        return
    if not (0 <= x1 < n and 0 <= y1 < m):
        is_first_drop = True

    if not (0 <= x2 < n and 0 <= y2 < m):
        is_second_drop = True

    if is_first_drop and is_second_drop:
        return

    elif (is_first_drop and not is_second_drop) or (not is_first_drop and is_second_drop):
        answer = min(count,answer)
        return

    for k in range(4):
        nx1 = x1 + dx[k]
        ny1 = y1 + dy[k]
        nx2 = x2 + dx[k]
        ny2 = y2 + dy[k]
        if not (0 <= nx1 < n and 0 <= ny1 < m) or not (0 <= nx2 < n and 0 <= ny2 < m):
            dfs(nx1,ny1,nx2,ny2,count+1)

        elif not check_first[nx1][ny1] and not check_second[nx2][ny2]:
            if a[nx1][ny1] == "#" and a[nx2][ny2] != "#":
                check_second[nx2][ny2] = True
                dfs(x1, y1, nx2, ny2, count + 1)
                check_second[nx2][ny2] = False
            elif a[nx1][ny1] != "#" and a[nx2][ny2] == "#":
                check_first[nx1][ny1] = True
                dfs(nx1,ny1,x2,y2,count+1)
                check_first[nx1][ny1] = False
            elif a[nx1][ny1] != "#" and a[nx2][ny2] != "#":
                check_first[nx1][ny1] = True
                check_second[nx2][ny2] = True
                dfs(nx1, ny1, nx2, ny2, count + 1)
                check_first[nx1][ny1] = False
                check_second[nx2][ny2] = False

dfs(first_coin[0],first_coin[1],second_coin[0],second_coin[1],0)

if answer > 10:
    print(-1)
else:
    print(answer)
