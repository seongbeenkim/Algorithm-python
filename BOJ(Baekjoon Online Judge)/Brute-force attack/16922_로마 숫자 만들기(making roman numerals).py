#https://www.acmicpc.net/problem/16922

import sys

n = int(sys.stdin.readline())
maximum = (50*20+1)
check = [False] * maximum
num = [1,5,10,50]
ans = 0

def go(i,start,res):
    global ans

    if i == n:
        if not check[res]:
            ans+=1
            check[res] = True
        return

    for j in range(start,4):
        go(i+1,j,res+num[j])

go(0,0,0)
print(ans)