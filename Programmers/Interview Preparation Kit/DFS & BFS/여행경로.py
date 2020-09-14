#https://programmers.co.kr/learn/courses/30/lessons/43164

import sys

sys.setrecursionlimit(10 ** 6)

answer = []
def dfs(index, i, ans, a, n):
    global answer

    if len(ans) == n + 1:
        answer = ans
        return True

    if i not in a:
        return False

    for j in range(len(a[i])):
        if a[i][j] != 'None':
            temp = a[i][j]
            a[i][j] = 'None'
            if dfs(index + 1, temp, ans + [temp], a, n):
                return True
            a[i][j] = temp



def solution(tickets):
    global answer
    a = dict()
    for i, j in tickets:
        if i not in a:
            a[i] = []
            a[i].append(j)
        else:
            a[i].append(j)
    for i in a:
        a[i].sort()
    dfs(0, "ICN", ["ICN"], a, len(tickets))

    return answer


print(solution([["ICN", "COO"], ["ICN", "BOO"], ["COO", "ICN"], ["BOO", "DOO"]]))


