#https://www.acmicpc.net/problem/15683

import sys
from copy import deepcopy

sys.setrecursionlimit(10**6)

n,m = map(int,sys.stdin.readline().split())
a = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

rotate = [4,2,4,4,1]
candi = []
ans = n*m

dx = [0,1,0,-1]
dy = [1,0,-1,0]

for i in range(n):
    for j in range(m):
        if 1 <= a[i][j] <= 5:
            candi.append((a[i][j],i,j))

def check(map,x,y,dir):
    i,j = x,y
    while 0 <= i < n and 0 <= j < m:
        if a[i][j] == 6:
            break
        map[i][j] = a[x][y]
        i += dx[dir]
        j += dy[dir]

def go(index,dirs):

    if index == len(candi):
        map = deepcopy(a)
        for i, (c, x, y) in enumerate(candi):
            if c == 1:
                check(map,x,y,dirs[i])
            elif c == 2:
                check(map,x,y,dirs[i])
                check(map, x, y, (dirs[i]+2)%4)
            elif c == 3:
                check(map,x,y,dirs[i])
                check(map, x, y, (dirs[i] + 1) % 4)
            elif c == 4:
                check(map,x,y,dirs[i])
                check(map, x, y, (dirs[i] + 1) % 4)
                check(map, x, y, (dirs[i] + 2) % 4)
            elif c == 5:
                check(map,x,y,dirs[i])
                check(map, x, y, (dirs[i] + 1) % 4)
                check(map, x, y, (dirs[i] + 2) % 4)
                check(map, x, y, (dirs[i] + 3) % 4)
        cnt = 0
        global ans
        for i in range(n):
            for j in range(m):
                if map[i][j] == 0:
                    cnt += 1
        if ans > cnt:
            ans = cnt
        return

    for i in range(4):
        go(index + 1, dirs + [i])

go(0,[])
print(ans)