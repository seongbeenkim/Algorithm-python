# https://programmers.co.kr/learn/courses/30/lessons/12931

def solution(n):
    answer = 0

    while n > 0:
        k = n % 10
        answer += k
        n //= 10
    return answer

print(solution(123))
print(solution(987))
