#https://www.acmicpc.net/problem/16637

import sys

n = int(sys.stdin.readline())
a = list(sys.stdin.readline().rstrip())
for i in range(0,n,2):
    a[i] = int(a[i])

m = (n-1) // 2 # 연산자 개수
ans = -2147383646

for s in range(1<<m): # m개의 연산자의 모든 경우의 수
    ok = True
    for i in range(m-1):
        if (s & (1<<i)) > 0 and (s & (1<<i+1)) > 0: # 연속적인 두 개의 연산자가 선택된 경우
            ok = False
            break

    if not ok:
        continue

    b = a.copy()

    for i in range(m):
        if ((s & (1<<i)) > 0): # 선택된 연산자들 앞, 뒤 피연산자들 먼저 계산
            k = (2*i)+1
            if b[k] == '+':
                b[k-1] += b[k+1]
                b[k+1] = 0
            elif b[k] == '-':
                b[k-1] -= b[k+1]
                b[k] = '+'
                b[k+1] = 0
            elif b[k] == '*':
                b[k-1] *= b[k+1]
                b[k] = '+'
                b[k+1] = 0

    temp = b[0]
    for i in range(m): # 모든 연산자들 앞, 뒤 피연산자들 계산
        k = (2*i)+1
        if b[k] == '+':
            temp += b[k+1]
        elif b[k] == '-':
            temp -= b[k+1]
        elif b[k] == '*':
            temp *= b[k+1]

    ans = max(ans,temp)

print(ans)