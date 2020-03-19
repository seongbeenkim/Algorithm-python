#acmicpc.net/problem/17070

import sys
from collections import deque
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())
a = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

ans = 0

def go(x,y,type):
    global ans
    if x == n-1 and y == n-1:
        ans += 1
        return
    if type == 0: # -
        if y + 1 < n and a[x][y+1] == 0:
            go(x,y+1,0)
        if x+1 < n and y + 1 < n and a[x][y + 1] == 0 and a[x + 1][y] == 0 and a[x + 1][y + 1] == 0:
            go(x+1,y+1, 1)

    elif type == 1: # diagonal
        if y + 1 < n and a[x][y+1] == 0:
            go(x,y+1,0)
        if x + 1 < n and a[x+1][y] == 0:
            go(x+1,y,2)
        if x+1 < n and y + 1 < n and a[x][y+1] == 0 and a[x+1][y] == 0 and a[x+1][y+1] == 0:
            go(x+1,y+1, 1)

    elif type == 2: # |
        if x + 1 < n and a[x+1][y] == 0:
            go(x+1,y,2)
        if x+1 < n and y + 1 < n and a[x+1][y+1] == 0 and a[x][y+1] == 0 and a[x+1][y] == 0:
            go(x+1,y+1,1)

go(0,1,0)
print(ans)