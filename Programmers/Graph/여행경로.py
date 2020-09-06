#https://programmers.co.kr/learn/courses/30/lessons/43164
### 1번 테스트 케이스 통과 못함..
import sys

sys.setrecursionlimit(10 ** 6)

def dfs(index, i, ans, a, n):
    if len(ans) == n + 1:
        return ans

    answer = []

    if i not in a:
        return []

    for j in range(len(a[i])):
        if a[i][j] != 'None':
            temp = a[i][j]
            a[i][j] = 'None'
            res = dfs(index + 1, temp, ans + [temp], a, n)
            if len(res) > len(answer):
                answer = res
                if len(answer) == n+1:
                    return answer
            a[i][j] = temp



def solution(tickets):
    a = dict()
    for i, j in tickets:
        if i not in a:
            a[i] = []
            a[i].append(j)
        else:
            a[i].append(j)
    for i in a:
        a[i].sort()
    answer = []
    temp = dfs(0, "ICN", ["ICN"], a, len(tickets))

    if len(temp) > len(answer):
        answer = temp
    return answer


print(solution([["ICN", "COO"], ["ICN", "BOO"], ["COO", "ICN"], ["BOO", "DOO"]]))


