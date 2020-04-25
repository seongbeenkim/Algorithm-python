#https://www.acmicpc.net/problem/2309

import sys

a = [int(sys.stdin.readline()) for _ in range(9)]
ans = sum(a)
a.sort()
def cnt():
    for i in range(9):
        for j in range(i + 1, 9):
            if ans - a[i] - a[j] == 100:
                for k in range(9):
                    if i == k or j == k:
                        continue
                    print(a[k])
                return
cnt()

"""
ans = []
candidate = []
def go(i,cnt,arr):
    if cnt == 7:
        if len(arr) == 7:
            if sum(arr) == 100:
                ans.append(sorted(arr))
    if i >= len(a):
        return
    go(i+1,cnt+1,arr+[a[i]])
    go(i+1,cnt,arr)

go(0,0,candidate)
print(*ans[0], sep="\n")
"""