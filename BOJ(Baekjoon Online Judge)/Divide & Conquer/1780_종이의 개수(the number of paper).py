#https://www.acmicpc.net/problem/1780

import sys

sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline())
a = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

minus_cnt = 0
zero_cnt = 0
plus_cnt = 0

def check(x,y,n):
    for i in range(x,x+n):
        for j in range(y,y+n):
            if a[x][y] != a[i][j]:
                return False

    return True

def go(x,y,k,n):
    global minus_cnt, zero_cnt, plus_cnt

    if k == 1:
        for i in range(x,x+3):
            for j in range(y,y+3):
                if a[i][j] == -1:
                    minus_cnt += 1
                elif a[i][j] == 0:
                    zero_cnt += 1
                else:
                    plus_cnt += 1
    else:
        for i in range(x,x+n,k):
            for j in range(y,y+n,k):
                if check(i, j, k):
                    if a[i][j] == -1:
                        minus_cnt += 1
                    elif a[i][j] == 0:
                        zero_cnt += 1
                    else:
                        plus_cnt += 1
                else:
                    go(i,j,k//3,k)

if check(0,0,n):
    if a[0][0] == -1:
        minus_cnt += 1
    elif a[0][0] == 0:
        zero_cnt += 1
    else:
        plus_cnt += 1
else:
    go(0,0,n//3,n)

print(minus_cnt,zero_cnt,plus_cnt, sep = "\n")