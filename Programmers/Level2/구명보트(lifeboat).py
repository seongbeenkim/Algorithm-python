# https://programmers.co.kr/learn/courses/30/lessons/42885

from collections import deque


def solution(people, limit):
    answer = 0
    people.sort()
    people = deque(people)

    i = 0
    j = len(people) - 1

    while i < j:
        if people[i] + people[j] <= limit:
            i += 1
            j -= 1
            answer += 1
        else:
            j -= 1

    return len(people) - answer


print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))
