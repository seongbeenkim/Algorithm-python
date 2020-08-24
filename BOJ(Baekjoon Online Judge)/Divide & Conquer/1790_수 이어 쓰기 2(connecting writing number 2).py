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
    print(s[len(s) -1 - (l-k)])


"""
n, k = map(int,sys.stdin.readline().split())

ans = -1

def check(n,k):
    cur = 0
    limit = 0
    while n >= 10 ** cur:
        cur += 1
        limit += cur * 9 * (10**(cur-1))

    limit -= cur * 9 * (10**(cur-1))

    difference = n - (10**(cur-1)) + 1
    limit += difference * cur

    return True if limit >= k else False

if check(n,k):

    cur = 0
    number = 0

    while k > number:
        cur += 1
        number += cur * 9 * (10 ** (cur - 1))
    number -= cur * 9 * (10 ** (cur - 1))

    count = k - number

    start = 10 ** (cur - 1)

    difference = count // cur
    remain = count % cur

    start += difference

    if remain == 0:
        ans = list(str(start - 1))[-1]
    else:
        ans = list(str(start))[remain - 1]

print(ans)
"""