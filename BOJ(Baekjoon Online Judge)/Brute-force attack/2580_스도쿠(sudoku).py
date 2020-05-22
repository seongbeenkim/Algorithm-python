#https://www.acmicpc.net/problem/2580

import sys

n = 9
a = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
zeros = []
def check_row(x,k):
    for col in range(n):
        if a[x][col] == k:
            return False
    return True

def check_col(y,k):
    for row in range(n):
        if a[row][y] == k:
            return False
    return True

def check_box(x,y,k):
    dx = (x//3)*3
    dy = (y // 3) * 3
    for i in range(dx,dx+3):
        for j in range(dy,dy+3):
            if a[i][j] == k:
                return False
    return True

def go(index):
    if index == len(zeros):
        return True
    i,j = zeros[index][0], zeros[index][1]
    for k in range(1, 10):
        if check_row(i, k) and check_col(j, k) and check_box(i, j, k):
            a[i][j] = k
            if go(index+1):
                return True
            a[i][j] = 0

for i in range(n):
    for j in range(n):
        if a[i][j] == 0:
            zeros.append([i,j])
go(0)
for row in a:
    print(*row)