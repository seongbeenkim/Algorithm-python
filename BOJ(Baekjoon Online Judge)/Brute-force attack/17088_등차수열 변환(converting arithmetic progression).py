#https://www.acmicpc.net/problem/17088

import sys

n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))

if n == 1:
    print(0)
    exit(0)

answer = -1

for d1 in range(-1,2):
    for d2 in range(-1,2):
        cnt = 0
        if d1 != 0:
            cnt += 1
        if d2 != 0:
            cnt += 1
        b = a.copy()

        b[0] = b[0] + d1
        b[1] = b[1] + d2
        diff = b[1] - b[0]

        ok = True
        
        for i in range(2,n):
            if b[i] - b[i-1] == diff:
                continue
            elif b[i] - b[i-1] == diff + 1:
                b[i] -= 1
                cnt += 1
            elif b[i] - b[i-1] == diff -1:
                b[i] += 1
                cnt += 1
            else:
                ok = False
                break
        if ok:
            if answer == -1 or answer > cnt:
                answer = cnt
                
print(answer)