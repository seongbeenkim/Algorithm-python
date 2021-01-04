# https://programmers.co.kr/learn/courses/30/lessons/12912

def solution(a, b):
    answer = 0
    if a > b:
        a, b = b, a

    for number in range(a, b + 1):
        answer += number

    return answer


print(solution(3, 5))
print(solution(3, 3))
print(solution(5, 3))
