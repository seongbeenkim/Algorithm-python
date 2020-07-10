#https://www.acmicpc.net/problem/9613

import sys
from itertools import combinations

n = int(sys.stdin.readline())
def gcd(x,y):
    if y == 0:
        return x
    else:
        return gcd(y,x%y)

for _ in range(n):
    number = list(map(int,sys.stdin.readline().split()))
    combi = combinations(number[1:],2)
    ans = 0
    for a,b in combi:
        ans += gcd(a,b)
    print(ans)