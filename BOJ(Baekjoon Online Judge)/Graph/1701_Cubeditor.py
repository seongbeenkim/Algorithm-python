#https://www.acmicpc.net/problem/1701

import sys

s = sys.stdin.readline().rstrip()

def pre_processing(s):
    n = len(s)
    fail = [0] * n
    j = 0
    for i in range(1,n):
        while j > 0 and s[i] != s[j]:
            j = fail[j-1]
        if s[i] == s[j]:
            fail[i] = j + 1
            j += 1
        else:
            fail[i] = 0

    return fail

ans = -1
for i in range(len(s)):
    arr = pre_processing(s[i:])
    ans = max(max(arr),ans)
print(ans)