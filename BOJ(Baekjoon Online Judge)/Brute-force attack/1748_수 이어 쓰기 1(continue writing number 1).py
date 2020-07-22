#https://www.acmicpc.net/problem/1748

import sys

n = int(sys.stdin.readline())
ans = 0
start = 1
length = 1
while start <= n:
    end = start*10 - 1
    if end > n:
        end = n
    ans += (end-start+1)*length
    length+=1
    start*=10
print(ans)

"""
ans = 0
mod = 10
length = 1
mul = 9
while mod <= n:
    ans += (length*mul)
    length += 1
    mul *= 10
    mod *= 10
ans += (n-(mod//10)+1) * length
print(ans)
"""

"""
n = int(sys.stdin.readline())
ans = 0
limit = len(str(n))

for i in range(1,limit):
    ans += i*(9*pow(10,i-1))
ans += limit*(n-pow(10,limit-1)+1)
print(ans)
"""