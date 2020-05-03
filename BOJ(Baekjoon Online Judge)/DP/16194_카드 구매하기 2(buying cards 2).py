#https://www.acmicpc.net/problem/16194
import sys

n = int(sys.stdin.readline())

p = [0] + list(map(int,sys.stdin.readline().split()))
d = [-1] * (n + 1)
d[0] = 0
d[1] = p[1]
for i in range(2, n+1):
    for j in range(1, i+1):
        if d[i] == -1 or d[i] > d[i-j] + p[j]:
            d[i] = d[i - j] + p[j]
print(d[n])

"""
d = [1000*10000] * (n+1)
d[0] = 0
d[1] = p[1]
for i in range(2,n+1):
    for j in range(1,i+1):
        d[i] = min(d[i],p[j]+d[i-j])
print(d[n])
"""