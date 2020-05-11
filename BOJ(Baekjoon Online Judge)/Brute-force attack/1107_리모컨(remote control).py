#https://www.acmicpc.net/problem/1107

import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
if m > 0:
    broken = list(map(int,sys.stdin.readline().split()))
else:
    broken = []

ans = abs(n-100)

def okay(i):
    cnt = 0
    if i == 0:
        if i not in broken:
            return 1
        else:
            return 0

    while i > 0:
        x = i % 10
        if x in broken:
            return 0
        else:
            i //= 10
            cnt+=1
    return cnt

for i in range(1000001):
    res = okay(i)
    if res > 0:
        ans = min(ans,abs(n-i)+res)

print(ans)