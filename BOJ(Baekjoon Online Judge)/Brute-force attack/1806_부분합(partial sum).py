#https://www.acmicpc.net/problem/1806

import sys

n, s = map(int,sys.stdin.readline().split())
a = list(map(int,sys.stdin.readline().split()))

ans = 214748367
left = 0
right = 0
sum = a[0]

while left <= right and right < n:
    if sum > s:
        ans = min(ans,right-left+1)
        sum -= a[left]
        left+=1
        if left>right and left < n:
            right = left
            sum = a[left]

    elif sum == s:
        ans = min(ans, right-left+1)
        right += 1
        if right < n:
            sum += a[right]

    else:
        right += 1
        if right < n:
            sum += a[right]
if ans == 214748367:
    print(0)
else:
    print(ans)
