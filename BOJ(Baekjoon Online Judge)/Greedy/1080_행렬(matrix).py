#https://www.acmicpc.net/problem/1080

import sys

n, m = map(int,sys.stdin.readline().split())
a = [list(map(int,sys.stdin.readline().rstrip())) for _ in range(n)]
b = [list(map(int,sys.stdin.readline().rstrip())) for _ in range(n)]

dx = [0,0,0,1,1,1,2,2,2]
dy = [0,1,2,0,1,2,0,1,2]

def check():
    cnt = 0

    for i in range(n-3+1):
        for j in range(m-3+1):
            if a[i][j] != b[i][j]:
                for k in range(9):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    a[nx][ny] = 1 - a[nx][ny]
                cnt += 1

    if a != b:
        return -1

    return cnt
print(check())

"""
cnt = 0

for i in range(n-2):
    for j in range(m-2):
        if a[i][j] == b[i][j]:
            continue
        else:
            cnt += 1
            for x in range(i,i+3):
                for y in range(j,j+3):
                    a[x][y] = 1 - a[x][y]

for i in range(n):
    for j in range(m):
        if a[i][j] != b[i][j]:
            cnt = -1
print(cnt)
"""