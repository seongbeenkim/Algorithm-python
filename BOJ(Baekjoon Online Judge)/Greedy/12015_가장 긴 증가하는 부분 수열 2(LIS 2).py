#https://www.acmicpc.net/problem/12015

import sys

n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
ans = []
cnt = 0

def lower_bound(x):
    i = 0
    j = len(ans) - 1

    while i <= j:
        mid = (i+j) // 2
        if ans[mid] == x:
            j = mid - 1
        elif ans[mid] > x:
            j = mid - 1
        else:
            i = mid + 1

    return i

for i in range(n):
    if not ans:
        ans.append(a[i])
    else:
        if ans[cnt] < a[i]:
            ans.append(a[i])
            cnt += 1
        else:
            x = lower_bound(a[i])
            ans[x] = a[i]

print(len(ans))