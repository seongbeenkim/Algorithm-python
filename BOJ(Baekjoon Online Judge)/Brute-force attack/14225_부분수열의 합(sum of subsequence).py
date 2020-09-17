#https://www.acmicpc.net/problem/14225

import sys
sys.setrecursionlimit(10**5)

n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
check = [False] * (100000 * 20)

def dfs(index,res):

    if index == n:
        check[res] = True
        return

    dfs(index+1, res + a[index])
    dfs(index + 1, res)

dfs(0,0)

for i in range(1,len(check)):
    if check[i] == False:
        print(i)
        break