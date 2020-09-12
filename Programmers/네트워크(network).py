#https://programmers.co.kr/learn/courses/30/lessons/43162

from collections import deque


def solution(n, computers):
    answer = 0
    check = [False] * n

    def bfs(i):
        q = deque()
        q.append(i)
        check[i] = True

        while q:
            x = q.popleft()
            for k in range(n):
                if computers[x][k] == 1 and not check[k]:
                    q.append(k)
                    check[k] = True

    for i in range(n):
        if not check[i]:
            bfs(i)
            answer += 1
    return answer