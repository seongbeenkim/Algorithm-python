#https://www.acmicpc.net/problem/9663

import sys

n = int(sys.stdin.readline())
a = [[False] * n for _ in range(n)]
check_col = [False] * n
check_dig = [False] * (2*n-1)
check_dig2 = [False] * (2*n-1)

def check(row,col):
    if check_col[col]:
        return False
    if check_dig[row+col]:
        return False
    if check_dig2[row-col+n-1]:
        return False
    return True

def go(row):
    if row == n:
        return 1
    ans = 0
    for col in range(n):
        if check(row,col):
            check_dig[row+col] = True
            check_dig2[row-col+n-1] = True
            check_col[col] = True
            a[row][col] = True
            ans += go(row+1)
            check_dig[row+col] = False
            check_dig2[row-col+n-1] = False
            check_col[col] = False
            a[row][col] = False
    return ans
print(go(0))


"""
n = int(sys.stdin.readline())

col = [False] * n
left_dig = [False] * (2*n-1)
right_dig = [False] * (2*n-1)

def dfs(i):

    if i == n:
        return 1
    ans = 0
    for j in range(n):
        if not col[j] and not left_dig[i+j] and not right_dig[i-j+n-1]:
            col[j] = left_dig[i+j] = right_dig[i-j+n-1] = True
            ans += dfs(i+1)
            col[j] = left_dig[i+j] = right_dig[i-j+n-1] = False

    return ans
print(dfs(0))
"""