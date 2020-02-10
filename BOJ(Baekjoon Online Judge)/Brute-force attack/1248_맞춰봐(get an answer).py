#https://www.acmicpc.net/problem/1248

import sys

n = int(sys.stdin.readline())
op = sys.stdin.readline()
s = [[0] * n for i in range(n)]
ans = [0] * n
cnt = 0
for i in range(n):
    for j in range(i,n):
        if op[cnt] == "0":
            s[i][j] = 0
        elif op[cnt] == "-":
            s[i][j] = -1
        else:
            s[i][j] = 1
        cnt += 1

def ok():
    for i in range(n):
        sum = 0
        for j in range(i,n):
            sum += ans[j]
            if s[i][j] == 0:
                if sum != 0:
                    return False
            elif s[i][j] < 0:
                if sum >= 0:
                    return False
            elif s[i][j] > 0:
                if sum <= 0:
                    return False
    return True

def go(index):
    if index == n:
        return ok()

    if s[index][index] == 0:
        ans[index] = 0
        return go(index+1)

    for i in range(1,11):
        ans[index] = i * s[index][index]
        if (go(index+1)):
            return True

    return False

go(0)
print(' '.join(map(str,ans)))