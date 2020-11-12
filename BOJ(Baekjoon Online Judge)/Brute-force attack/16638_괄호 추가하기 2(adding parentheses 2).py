#https://www.acmicpc.net/problem/16638

import sys

n = int(sys.stdin.readline())
a = list(sys.stdin.readline().rstrip())
for i in range(0,n,2):
    a[i] = int(a[i])

m = (n-1) // 2 # 연산자 개수

MIN = -2147383647
answer = MIN

for s in range(1<<m):
    b = a.copy()
    result = 0
    parentheses = []
    is_sequence = False

    for i in range(m-1):
        if (s & (1<<i)) > 0 and (s & (1<<i+1)) > 0: # 해당 연산자에 괄호 넣을지 판단하는 비트마스킹
            is_sequence = True
            break

    if is_sequence:
        continue

    for i in range(m): # 괄호 연산
        if (s & (1<<i)) <= 0:
            continue
        parentheses.append(i*2+1)
        k = i*2+1
        if b[k] == '+':
            b[k-1] += b[k + 1]
            b[k] = '0'
            b[k+1] = 0
        elif b[k] == '-':
            b[k-1] -= b[k + 1]
            b[k] = '0'
            b[k+1] = 0
        else:
            b[k-1] *= b[k + 1]
            b[k] = '0'
            b[k+1] = 0
    temp = []

    j = 0
    while j < n:
        if j % 2 == 0:
            temp.append(b[j])
        else:
            if b[j] == '0':
                j+=1
            else:
                if b[j] == '*':
                    num = temp[-1] * b[j + 1]
                    temp.pop()
                    temp.append(num)
                    j+=1

                else:
                    temp.append(b[j])
        j += 1

    b = temp
    l = len(b)
    result = b[0]

    for i in range(1,l,2):
        if b[i] == "+":
            result += b[i+1]
        elif b[i] == "-":
            result -= b[i+1]
    answer = max(result,answer)

print(answer)