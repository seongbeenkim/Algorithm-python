#https://www.acmicpc.net/problem/17087

import sys
from collections import deque

n, s = map(int,sys.stdin.readline().split())
a = list(map(int,sys.stdin.readline().split()))
candi = []
d = 0

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

for i in range(n):
    temp = s - a[i]
    if temp < 0:
        temp = -temp
    candi.append(temp)

ans = candi[0]
for i in range(1,n):
    ans = gcd(ans,candi[i])
print(ans)