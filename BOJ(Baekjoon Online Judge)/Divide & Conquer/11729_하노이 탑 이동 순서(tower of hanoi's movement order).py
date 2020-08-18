#https://www.acmicpc.net/problem/11729

import sys
sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline())
ans = []

def move(n,x,y):
    if n == 0:
        return
    move(n-1,x,6-x-y)
    ans.append((x,y))
    move(n-1,6-x-y,y)
move(n,1,3)

print(len(ans))
for x,y in ans:
    print(x,y)