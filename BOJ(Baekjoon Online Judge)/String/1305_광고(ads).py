#https://www.acmicpc.net/problem/1305

import sys

l = int(sys.stdin.readline())
t = sys.stdin.readline().strip()
n = len(t)
fail = [0] * n
def pre_processing():
    j = 0
    for i in range(1,n):
        while j > 0 and t[i] != t[j]:
            j =fail[j-1]
        if t[i] == t[j]:
            fail[i] = j+1
            j += 1
        else:
            fail[i] = 0

pre_processing()
print(l-fail[l-1])