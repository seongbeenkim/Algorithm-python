#https://www.acmicpc.net/problem/17298

import sys

n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
stack = []
ans = [-1] * n

for i in range(len(a)):
    while stack and a[stack[-1]] < a[i]:
        ans[stack.pop()] = a[i]
    stack.append(i)
print(*ans)