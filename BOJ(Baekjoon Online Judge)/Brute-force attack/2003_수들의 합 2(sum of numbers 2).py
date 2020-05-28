#https://www.acmicpc.net/problem/2003

import sys

n, m = list(map(int,sys.stdin.readline().split()))
a = list(map(int,sys.stdin.readline().split()))
left = 0
right = 0
sum = a[left]
cnt = 0
while (left <= right and right < n):
    if sum > m:
        sum -= a[left]
        left += 1
        if left > right and left < n:
            right = left
            sum = a[left]
    elif sum < m:
        right += 1
        if right < n:
            sum += a[right]
    else:
        cnt += 1
        right += 1
        if right < n:
            sum += a[right]
print(cnt)


"""
i = 0
j = 0

while j < n:
    if i == j:
        if a[i] == m:
            ans += 1
        j += 1

    elif i < j:
        total = sum(a[i:j+1])
        if total == m:
            ans += 1
            j+=1
        elif total > m:
            i+=1
        elif total < m:
            j+=1

print(ans)
"""