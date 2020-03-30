#https://www.acmicpc.net/problem/1790

import sys

n, k = map(int,sys.stdin.readline().split())
ans = 0
left = 1
right = n

def cal(n):
    ans = 0
    length = 1
    start = 1
    while start <= n:
        end = (start*10)-1
        if end > n:
            end = n
        ans += (end-start+1) * length
        length += 1
        start *= 10
    return ans


if cal(n) < k:
    print(-1)
else:
    while left <= right:
        mid = (left + right) // 2
        length = cal(mid)
        if length < k:
            left = mid+1
        else:
            ans = mid
            right = mid - 1
    s = str(ans)
    l = cal(ans)
    print(s[len(s) -1 - (l-k)] )