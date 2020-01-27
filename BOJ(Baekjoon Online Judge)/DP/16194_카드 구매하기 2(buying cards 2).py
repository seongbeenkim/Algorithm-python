#https://www.acmicpc.net/problem/16194
import sys

n = int(sys.stdin.readline())
d = [-1] * (n + 1)
d[0] = 0
p = [0] * (n + 1)
price = list(map(int,sys.stdin.readline().split()))
for i, item in enumerate(price):
    p[i+1] = item
for i in range(1, n+1):
    for j in range(1, i+1):
        if d[i] == -1 or d[i] > d[i-j] + p[j]:
            d[i] = d[i - j] + p[j]
print(d[n])