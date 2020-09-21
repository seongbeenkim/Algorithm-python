#https://www.acmicpc.net/problem/16928

import sys
from collections import deque

n, m = map(int,sys.stdin.readline().split())

ladders = {}
for _ in range(n):
    x, y = map(int,sys.stdin.readline().split())
    ladders[x] = y

snakes = {}
for _ in range(m):
    x, y = map(int,sys.stdin.readline().split())
    snakes[x] = y

d = [-1] * 101

q = deque()
q.append(1)
d[1] = 0

while q:
    x = q.popleft()
    for i in range(1,7):
        y = x + i
        if y <= 100:
            if y in ladders:
                y = ladders[y]
            elif y in snakes:
                y = snakes[y]
            if d[y] == -1 or d[y] > d[x] + 1:
                d[y] = d[x] + 1
                q.append(y)
"""
while q:
    x = q.popleft()
    for i in range(1,7):
        y = x + i
        if y <= 100:
            if y in ladders:
                if d[ladders[y]] == -1 or d[ladders[y]] > d[x] + 1:
                    d[ladders[y]] = d[x] + 1
                    q.append(ladders[y])
            elif y in snakes:
                if d[snakes[y]] == -1 or d[snakes[y]] > d[x] + 1:
                    d[snakes[y]] = d[x] + 1
                    q.append(snakes[y])
            elif d[y] == -1 or d[y] > d[x] + 1:
                d[y] = d[x] + 1
                q.append(y)
"""

# 아래의 코드는 22% 실패... why?
"""
while q:
    x = q.popleft()
    for i in range(1,7):
        y = x + i
        if y <= 100:
            if y in ladders and (d[ladders[y]] == -1 or d[ladders[y]] > d[x] + 1):
                d[ladders[y]] = d[x] + 1
                q.append(ladders[y])
            elif y in snakes and (d[snakes[y]] == -1 or d[snakes[y]] > d[x] + 1):
                d[snakes[y]] = d[x] + 1
                q.append(snakes[y])
            elif d[y] == -1 or d[y] > d[x] + 1:
                d[y] = d[x] + 1
                q.append(y)
"""
print(d[100])