#https://www.acmicpc.net/problem/15684

import sys
from copy import deepcopy

m, k, n = map(int,sys.stdin.readline().split())
ladder = [[0] * (m) for _ in range(n)]
MAX = 2147383647
answer = MAX

for _ in range(k):
    x, y = map(int,sys.stdin.readline().split())
    x-=1
    y-=1
    ladder[x][y] = 1

def check():
    for i in range(m):
        y = i
        for x in range(n):
            if ladder[x][y] == 1:
                y += 1
            elif y-1 >= 0 and ladder[x][y-1] == 1:
                y -= 1
        if y != i:
            return False
    return True

def go(x, cnt):
    global answer
    if cnt > 3:
        return 
    if check():
        answer = min(cnt,answer)
        return 
    
    for i in range(x,n):
        for j in range(m-1):
            if ladder[i][j]:
                continue
            if j-1 >= 0 and ladder[i][j-1]:
                continue
            if j+1 < m and ladder[i][j+1]:
                continue
            ladder[i][j] = 1
            go(i,cnt+1)
            ladder[i][j] = 0
go(0,0)
if answer != MAX:
    print(answer)
else:
    print(-1)