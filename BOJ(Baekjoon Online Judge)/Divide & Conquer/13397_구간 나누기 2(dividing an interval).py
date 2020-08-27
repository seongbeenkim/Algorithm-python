#https://www.acmicpc.net/problem/13397

import sys

n, m = map(int,sys.stdin.readline().split())

a = list(map(int,sys.stdin.readline().split()))

l = 0
r = max(a) - min(a)
ans = 2147383647

def check(mid):
    cnt = 1
    maximum = a[0]
    minimum = a[0]

    for x in a[1:]:
        maximum = max(x, maximum)
        minimum = min(x, minimum)
        if maximum - minimum > mid:
            cnt += 1
            maximum = x
            minimum = x

    return cnt <= m


while l <= r:
    mid = (l+r) // 2
    if check(mid):
        ans = mid
        r = mid - 1
    else:
        l = mid + 1

print(ans)