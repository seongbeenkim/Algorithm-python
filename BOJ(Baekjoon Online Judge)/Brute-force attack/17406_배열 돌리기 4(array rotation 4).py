#https://www.acmicpc.net/problem/17406

import sys
from copy import deepcopy

n, m, k = map(int,sys.stdin.readline().split())
a = []
op = []
check = [False] * k
MIN = 50*100
answer = MIN

for _ in range(n):
    a.append(list(map(int,sys.stdin.readline().split())))

for _ in range(k):
    r, c, s = map(int,sys.stdin.readline().split())
    r -= 1
    c -= 1
    op.append((r,c,s))
op.sort()

def next_permutation(a):
    i = len(a) - 1
    while i > 0 and a[i-1] >= a[i]:
        i -= 1
    if i <= 0:
        return False

    j = len(a) - 1
    while a[i-1] >= a[j]:
        j -= 1

    a[i-1],a[j] = a[j],a[i-1]

    j = len(a) - 1
    while i <= j:
        a[i],a[j] = a[j],a[i]
        i+=1
        j-=1
    return True

def rotate(operator,arr):
    x = operator[0]
    y = operator[1]
    d = operator[2]

    s_x = x-d
    s_y = y-d
    e_x = x+d
    e_y = y+d

    while s_x != e_x and s_y != e_y:
        start = arr[s_x][s_y]
        for i in range(s_x,e_x):
            arr[i][s_y] = arr[i+1][s_y]
        for j in range(s_y,e_y):
            arr[e_x][j] = arr[e_x][j+1]
        for i in range(e_x,s_x,-1):
            arr[i][e_y] = arr[i-1][e_y]
        for j in range(e_y,s_y,-1):
            arr[s_x][j] = arr[s_x][j-1]

        arr[s_x][s_y+1] = start
        s_x += 1
        s_y += 1
        e_x -= 1
        e_y -= 1

while True:
    arr = deepcopy(a)
    for operator in op:
        rotate(operator,arr)

    for i in range(n):
        answer = min(answer, sum(arr[i]))

    if not next_permutation(op):
        break
print(answer)