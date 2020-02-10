#https://www.acmicpc.net/problem/10973

import sys

n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
max = [0] * n
def go():
    i = n - 1

    while i > 0 and a[i] > a[i-1]:
        i -= 1

    if i <= 0:
        return False

    j = n - 1

    while a[j] >= a[i - 1]:
        j -= 1

    a[j], a[i - 1] = a[i - 1], a[j]

    j = n - 1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1

    return True

if go():
    print(" ".join(map(str,a)))
else:
    print(-1)