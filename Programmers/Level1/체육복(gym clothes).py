# https://programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    answer = 0
    count = dict()

    for i in range(n):
        count[i] = 1

    for i in lost:
        count[i - 1] -= 1

    for i in reserve:
        count[i - 1] += 1

    for i in range(n):
        if count[i] > 0:
            continue

        if i - 1 >= 0 and count[i - 1] > 1:
            count[i - 1] -= 1
            count[i] += 1
        elif i + 1 < n and count[i + 1] > 1:
            count[i + 1] -= 1
            count[i] += 1

    for i in range(n):
        if count[i] > 0:
            answer += 1

    return answer


print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5, [2, 4], [3]))
print(solution(3, [3], [1]))
