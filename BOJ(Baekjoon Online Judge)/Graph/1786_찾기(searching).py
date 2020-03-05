#https://www.acmicpc.net/problem/1786

import sys

T = sys.stdin.readline().rstrip()
P = sys.stdin.readline().rstrip()

fail = [0] * len(P)
n = len(T)
m = len(P)

def pre_processing():
    j = 0
    for i in range(1,m):
        while j > 0 and P[i] != P[j]:
            j = fail[j-1]
        if P[i] == P[j]:
            fail[i] = j+1
            j += 1
        else:
            fail[i] = 0

def kmp():
    j = 0
    ans = []
    for i in range(n):
        while j > 0 and T[i] != P[j]:
            j = fail[j-1]
        if T[i] == P[j]:
            if j == m-1:
                ans.append(i-m+1)
                j = fail[j]
            else:
                j += 1

    return ans

pre_processing()
ans = kmp()

print(len(ans))
for i in ans:
    print(i+1)