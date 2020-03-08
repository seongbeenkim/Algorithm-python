#https://www.acmicpc.net/problem/11399

import sys

n = int(sys.stdin.readline())
p = list(map(int,sys.stdin.readline().split()))

p.sort()

sum = 0
ans = 0
for i in p:
    sum += i
    ans += sum
print(ans)