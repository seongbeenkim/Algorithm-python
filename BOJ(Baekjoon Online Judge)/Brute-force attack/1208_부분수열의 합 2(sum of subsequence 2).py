#https://www.acmicpc.net/problem/1208

import sys

n, s = list(map(int,sys.stdin.readline().split()))
a = list(map(int,sys.stdin.readline().split()))
half = n//2
d1 = []
d2 = []
def go(index,end,sum,d):
    if index == end:
        d.append(sum)
        return
    go(index+1,end,sum+a[index],d)
    go(index+1,end,sum,d)
go(0,half,0,d1)
go(half,n,0,d2)
d1.sort()
d2.sort()
d2.reverse()
l = 0
r = 0
ans = 0
while l < len(d1) and r < len(d2):
    sum = d1[l] + d2[r]
    if sum == s:
        c1 = 1
        c2 = 1
        l += 1
        r += 1
        while l < len(d1) and d1[l] == d1[l-1]:
            l += 1
            c1 += 1
        while r < len(d2) and d2[r] == d2[r-1]:
            r += 1
            c2 += 1
        ans += c1 * c2
    elif sum > s:
        r += 1
    else:
        l += 1
if s == 0:
    ans -= 1
print(ans)