#https://programmers.co.kr/learn/courses/30/lessons/49189

from collections import deque

def solution(n, edge):
    a = [[] for _ in range(n + 1)]
    d = [0] * (n + 1)
    visit = [False] * (n + 1)
    for x, y in edge:
        a[x].append(y)
        a[y].append(x)

    q = deque()
    q.append(1)
    visit[1] = True
    while q:
        x = q.popleft()
        for y in a[x]:
            if not visit[y]:
                visit[y] = True
                d[y] = d[x] + 1
                q.append(y)
    farthest = max(d)
    answer = d.count(farthest)

    return answer

print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))