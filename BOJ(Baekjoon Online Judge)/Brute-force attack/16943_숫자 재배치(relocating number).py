#https://www.acmicpc.net/problem/16943

import sys

a, b = sys.stdin.readline().split()
a = list(a)
b = int("".join(b))

answer = -1

def next_permutation(a):
    i = len(a) - 1

    while i >= 0 and a[i-1] >= a[i]:
        i -= 1

    if i <= 0:
        return False
    
    j = len(a) - 1

    while a[i-1] >= a[j]:
        j -= 1

    a[i-1], a[j] = a[j], a[i-1]

    j = len(a) - 1

    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1

    return True

a.sort()

while True:

    if int("".join(a)) <= b and a[0] != '0':
        answer = int("".join(a))

    if next_permutation(a):
        if int("".join(a)) <= b and a[0] != '0':
            answer = max(int("".join(a)),answer)
    else:
        break
print(answer)