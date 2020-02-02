#https://www.acmicpc.net/problem/9095
import sys

t = int(sys.stdin.readline())

def go(n,sum):
    if sum == n:
        return 1
    if sum > n:
        return 0
    count = 0

    for i in range(1,4):
       count += go(n,sum+i)
    return count

for i in range(t):
    n = int(sys.stdin.readline())
    ans = go(n,0)
    print(ans)