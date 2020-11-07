#https://www.acmicpc.net/problem/1913

import sys

n = int(sys.stdin.readline())
find = int(sys.stdin.readline())

d = [[-1] * n for _ in range(n)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]

sx = n//2
sy = n//2


number = 1
dir = 0
d[sx][sy] = number
number += 1

i = 1
repeat = 0

while number < n*n:
    cnt = i

    if repeat == 2:
        i += 1
        cnt = i
        repeat = 0

    if dir == 0:
        while cnt > 0:
            sx += dx[dir]
            if sx == -1:
                break
            d[sx][sy] = number
            cnt -= 1
            number += 1
        dir = 1
        repeat += 1

    elif dir == 1:
        while cnt > 0:
            sy += dy[dir]
            d[sx][sy] = number
            cnt -= 1
            number += 1
        dir = 2
        repeat += 1

    elif dir == 2:
        while cnt > 0:
            sx += dx[dir]
            d[sx][sy] = number
            cnt -= 1
            number += 1
        dir = 3
        repeat += 1
    elif dir == 3:
        while cnt > 0:
            sy += dy[dir]
            d[sx][sy] = number
            cnt -= 1
            number += 1
        dir = 0
        repeat += 1

answer = [0,0]
for i in range(n):
    print(*d[i])
    for j in range(n):
        if d[i][j] == find:
            answer[0] = i + 1
            answer[1] = j + 1
print(*answer)