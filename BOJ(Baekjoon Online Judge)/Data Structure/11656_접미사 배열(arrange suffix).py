#https://www.acmicpc.net/problem/11656

import sys

s = sys.stdin.readline().rstrip()
ans = []

for i in range(len(s)):
    ans.append(s[i:])
ans.sort()
for i in ans:
    print(i)