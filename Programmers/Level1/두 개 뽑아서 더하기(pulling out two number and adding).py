# https://programmers.co.kr/learn/courses/30/lessons/68644

def solution(numbers):
    answer = set()
    n = len(numbers)

    for i in range(n):
        for j in range(i + 1, n):
            if i == j:
                continue
            answer.add(numbers[i] + numbers[j])

    answer = list(answer)
    answer.sort()
    return answer


print(solution([2, 1, 3, 4, 1, ]))
print(solution([5, 0, 2, 7]))
