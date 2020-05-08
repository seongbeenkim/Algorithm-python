#https://www.acmicpc.net/problem/11722
import sys

n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
d = [0] * n

d[0] = 1

for i in range(1,n):
    d[i] = 1
    for j in range(i-1, -1, -1):
        if a[j] > a[i] and d[i] < d[j] + 1:
            d[i] = d[j] + 1
print(max(d))