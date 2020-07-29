#https://www.acmicpc.net/problem/1248

import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline().rstrip()
op = [[0] * n for _ in range(n)]
ans = [0] * n

cnt = 0
for i in range(n):
    for j in range(i,n):
        if s[cnt] == "0":
            op[i][j] = 0
        elif s[cnt] == "+":
            op[i][j] = 1
        else:
            op[i][j] = -1
        cnt+=1

def check(index):
    sum = 0
    for i in range(index,-1,-1):
        sum += ans[i]

        if op[i][index] == 0 and sum != 0:
            return False
        elif op[i][index] == 1 and sum <= 0 :
            return False
        elif op[i][index] == -1 and sum >= 0:
            return False

    return True

def go(index):
    if index == n:
        return True

    if op[index][index] == 0:
        ans[index] = 0
        if check(index):
            if go(index+1):
                return True
        return False

    for i in range(1,11):
        ans[index] = i * op[index][index]
        if check(index):
            if go(index+1):
                return True

    return False

go(0)
print(*ans)