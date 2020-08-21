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
        go(x, y, mid_x, mid_y, cnt, next_add)  # 1분면
    elif x <= r <= mid_x and mid_y <= c <= des_y:
        go(x, mid_y+1, mid_x, des_y, cnt + add, next_add)  # 2분면
    elif mid_x <= r <= des_x and y <= c <= mid_y:
        go(mid_x+1, y, des_x, mid_y, cnt + add + add, next_add)  # 3분면
    elif mid_x <= r <= des_x and mid_y <= c <= des_y:
        go(mid_x+1, mid_y+1, des_x, des_y, cnt + add + add + add, next_add)  # 4분면


go(0, 0, max_index, max_index, 0, add)