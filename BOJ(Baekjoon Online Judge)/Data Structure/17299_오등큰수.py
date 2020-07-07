#https://www.acmicpc.net/problem/17299

import sys

n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
f = {}
for i in a:
    if i not in f:
        f[i] = 1
    else:
        f[i] += 1

stack = []
ans = [-1] * n

for i in range(n):
    while stack and f[a[stack[-1]]] < f[a[i]]:
        ans[stack.pop()] = a[i]
    stack.append(i)
print(*ans)