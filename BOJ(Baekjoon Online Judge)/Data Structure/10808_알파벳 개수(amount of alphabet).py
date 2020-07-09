#https://www.acmicpc.net/problem/10808

import sys

s = sys.stdin.readline().rstrip()
ans = [0] * 26

for i in s:
    ans[ord(i) - ord('a')] += 1

print(*ans)