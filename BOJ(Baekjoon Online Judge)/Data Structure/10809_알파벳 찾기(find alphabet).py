#https://www.acmicpc.net/problem/10809

import sys

s = sys.stdin.readline().rstrip()
ans = [-1] * 26

for i in range(len(s)):
    if ans[ord(s[i])-ord('a')] != -1:
        continue
    ans[ord(s[i])-ord('a')] = i

print(*ans)