#https://www.acmicpc.net/problem/10989

import sys

n = int(sys.stdin.readline())
d = [0] * 10001

for _ in range(n):
    x = int(sys.stdin.readline())
    d[x] += 1

for i in range(10001):
    if d[i] == 0:
        continue
    while d[i] > 0:
        print(i)
        d[i] -= 1