#https://www.acmicpc.net/problem/16198

import sys, copy

n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))

def dfs(array, res):
    answer = 0
    if len(array) == 2:
        return res

    n = len(array)

    for i in range(1,n-1):
        a = array.copy()
        temp = a[i-1] * a[i+1]
        del a[i]
        answer = max(dfs(a,res + temp),answer)

    return answer

print(dfs(a,0))
