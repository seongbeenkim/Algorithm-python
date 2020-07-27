#https://www.acmicpc.net/problem/14501

import sys
sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline())
t = [0] * (n+1)
p = [0] * (n+1)

for i in range(1,n+1):
    t[i], p[i] = map(int,sys.stdin.readline().split())

def go(day,sum):
    if day == n+1:
        return sum
    if day > n+1:
        return 0
    a = go(day + t[day],sum + p[day])
    b = go(day + 1,sum)

    return max(a,b)
print(go(1,0))
"""
def go(i,cnt):
    ans = 0
    if i == n:
        if t[i] != 1:
            return cnt
        else:
            return cnt+p[i]
    if i > n:
        return cnt

    if i+t[i] <= n+1:
        ans = max(ans,go(i+t[i],cnt+p[i]))
    ans = max(ans,go(i+1,cnt))
    return ans
"""

"""
ans = 0
def go(index,profit,v,n):
    global ans
    if index > n:
        temp = index-t[v]
        if t[v] + temp -1 > n:
            profit -= p[v]
        ans = max(ans,profit)
        return
    go(index+t[index],profit+p[index],index,n)
    go(index+1,profit,index,n)
go(1,0,0,n)
print(ans)
"""