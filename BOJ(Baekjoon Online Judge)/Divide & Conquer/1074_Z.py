#https://www.acmicpc.net/problem/1074

import sys
sys.setrecursionlimit(10**5)
# 10**6 이상으로 했을 때 메모리 초과, 10**5로 하면 기본(default = 10**4) 결과 값의 두 배의 메모리 크기가 된다.

n, r, c = map(int, sys.stdin.readline().split())

max_index = (2 ** n)-1
add = ((2 ** n) ** 2) // 4

def go(x, y, des_x, des_y, cnt,add):
    if x == des_x and y == des_y:
        if x == r and y == c:
            print(cnt)
        return

    mid_x = (x + des_x) // 2
    mid_y = (y + des_y) // 2

    next_add = add//4

    if x <= r <= mid_x and y <= c <= mid_y:
        go(x, y, mid_x, mid_y, cnt, next_add)  # 왼쪽 위
    elif x <= r <= mid_x and mid_y <= c <= des_y:
        go(x, mid_y+1, mid_x, des_y, cnt + add, next_add)  # 오른쪽 위
    elif mid_x <= r <= des_x and y <= c <= mid_y:
        go(mid_x+1, y, des_x, mid_y, cnt + add + add, next_add)  # 왼쪽 아래
    elif mid_x <= r <= des_x and mid_y <= c <= des_y:
        go(mid_x+1, mid_y+1, des_x, des_y, cnt + add + add + add, next_add)  # 오른쪽 아래


go(0, 0, max_index, max_index, 0, add)


"""
n, r, c = map(int,sys.stdin.readline().split())
dx = [0,0,1,1]
dy = [0,1,0,1]

MAX = (2**n)-1

def go(x,y,max_x,max_y,n,cnt):

    if n == 1:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx == r and ny == c:
                print(cnt)
                return
            cnt += 1
        return

    mid_x = (x+max_x)//2
    mid_y = (y+max_y)//2

    add = ((2**n)**2)//4

    if x <= r <= mid_x and y <= c <= mid_y:
        go(x,y,mid_x,mid_y,n-1,cnt) # 왼쪽 위
    elif x <= r <= mid_x and mid_y+1 <= c <= max_y:
        go(x, mid_y+1, mid_x, max_y, n-1, cnt+add) # 오른쪽 위
    elif mid_x + 1 <= r <= max_x and y <= c <= mid_y:
        go(mid_x + 1, y, max_x, mid_y, n-1, cnt+add+add) # 왼쪽 아래
    elif mid_x + 1 <= r <= max_x and mid_y + 1 <= c <= max_y:
        go(mid_x + 1, mid_y + 1, max_x, max_y, n-1, cnt+add+add+add) # 오른쪽 아래


go(0,0,MAX,MAX,n,0)
"""