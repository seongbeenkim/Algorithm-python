#https://www.acmicpc.net/problem/16945

import sys

n = 3
answer = 81
a = []
for _ in range(n):
    a += list(map(int,sys.stdin.readline().split()))
d = [i for i in range(1, 10)]

def calculate(d):

    compare_value = d[n*0] + d[n*1] + d[n*2]

    for i in range(n):
        if compare_value != d[i*n] + d[i*n+1] + d[i*n+2]:
            return False

    for i in range(n):
        if compare_value != d[0*n+i] + d[1*n+i] + d[2*n+i]:
            return False

    if compare_value != d[n*0+0] + d[n*1+1] + d[n*2+2]:
        return False

    if compare_value != d[n*0+2] + d[n*1+1] + d[n*2+0]:
        return False

    return True

def next_permutation(d):
    i = len(d)-1
    while i > 0 and d[i-1] >= d[i]:
        i -= 1

    if i == 0:
        return False

    j = len(d)-1
    while d[i-1] >= d[j]:
        j -= 1

    d[i-1], d[j] = d[j], d[i-1]

    j = len(d)-1
    while i < j:
        d[i], d[j] = d[j], d[i]
        i += 1
        j -= 1
    return True

while True:
    if calculate(d):
        result = 0
        for i in range(n*n):
            result += abs(a[i] - d[i])
        answer = min(answer,result)
    if not next_permutation(d):
        break
print(answer)