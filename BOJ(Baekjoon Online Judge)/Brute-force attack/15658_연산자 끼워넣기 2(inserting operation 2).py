#acmicpc.net/problem/15658

import sys
n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
plus,minus,mul,div = (map(int,sys.stdin.readline().split()))

ans = []
def go(i, total, plus, minus, mul, div):
    if i == n:
        ans.append(total)
        return
    if plus > 0:
         go(i+1,total+a[i], plus-1, minus, mul, div)
    if minus > 0:
        go(i+1,total-a[i], plus, minus-1, mul, div)
    if mul > 0:
        go(i+1,total*a[i], plus, minus, mul-1, div)
    if div > 0:
        if total >= 0:
            go(i+1,total//a[i], plus, minus, mul, div-1)
        else:
            go(i+1,-(abs(total)//a[i]), plus, minus, mul, div-1)
go(1,a[0],plus,minus,mul,div)
ans.sort()
print(ans[-1])
print(ans[0])
