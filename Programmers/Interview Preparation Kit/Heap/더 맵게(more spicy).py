#https://www.welcomekakao.com/learn/courses/30/lessons/42626

import heapq


def solution(scoville, K):
    answer = 0
    h = []

    for i in scoville:
        heapq.heappush(h, i)

    while True:
        if h[0] >= K:
            break
        else:
            if len(h) <= 1:
                answer = -1
                break
        if h:
            first = heapq.heappop(h)
        if h:
            second = heapq.heappop(h)

        heapq.heappush(h, first + (second * 2))
        answer += 1

    return answer