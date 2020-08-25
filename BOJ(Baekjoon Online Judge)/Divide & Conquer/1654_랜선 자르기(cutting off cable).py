#https://www.acmicpc.net/problem/1654

import sys

k,n = map(int,sys.stdin.readline().split())
a = []
for i in range(k):
    a.append(int(sys.stdin.readline()))

def check(num):
    cnt = 0
    for i in a:
        cnt += i // num
    return cnt

l = 1
r = max(a)

while l <= r:
    m = (l+r) // 2
    res = check(m)
    if res >= n:
        l = m+1
    else:
        r = m-1
print(r)


"""
k, n = map(int,sys.stdin.readline().split())
cable = [int(sys.stdin.readline()) for _ in range(k)]

total = 0

def check(length):
    total = 0
    for lan in cable:
        total += lan // length

    if total >= n:
        return True
    else:
        return False

start = 1
end = max(cable)
ans = 0
while start <= end:
    mid = (start+end) // 2
    if check(mid):
        ans = max(ans,mid)
        start = mid + 1
    else:
        end = mid - 1

print(ans)
"""