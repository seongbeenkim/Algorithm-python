#https://www.acmicpc.net/problem/16936

import sys

n = int(sys.stdin.readline())
b = list(map(int,sys.stdin.readline().split()))
b.sort()

answer = []
def dfs(idx,res):
    global answer

    if idx >= n:
        return False

    if len(res) == n:
        answer = res
        return True

    if res[-1] % 3 == 0 and res[-1] // 3 in b and res[-1] // 3 not in res:
        ans = dfs(idx+1,res+[res[-1] // 3])
        if ans != False:
            return ans

    if res[-1] * 2 in b and res[-1] * 2 not in res:
        ans = dfs(idx + 1, res + [res[-1]*2])
        if ans != False:
            return ans

    return False

for i in b:
    if dfs(0,[i]):
        break
print(*answer)