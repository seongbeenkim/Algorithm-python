#https://www.acmicpc.net/problem/11052
import sys

n = int(sys.stdin.readline())
p = [0] + list(map(int,sys.stdin.readline().split()))
d = [0] * (n + 1)

d[1] = p[1]

for i in range(2,n+1):
    for j in range(1,i+1):
        d[i] = max(d[i],p[j]+d[i-j])
print(d[n])