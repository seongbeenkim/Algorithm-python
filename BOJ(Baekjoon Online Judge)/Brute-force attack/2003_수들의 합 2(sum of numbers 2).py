#https://www.acmicpc.net/problem/2003

import sys

n, m = list(map(int,sys.stdin.readline().split()))
a = list(map(int,sys.stdin.readline().split()))
left = 0
right = 0
sum = a[left]
cnt = 0
while (left <= right and right <= n-1):
    if sum > m:
        sum -= a[left]
        left += 1
        if left > right and left < n:
            right = left
            sum = a[left]
    elif sum < m:
        right += 1
        if right <= n-1:
            sum += a[right]
    else:
        cnt += 1
        right += 1
        if right <= n-1:
            sum += a[right]
print(cnt)