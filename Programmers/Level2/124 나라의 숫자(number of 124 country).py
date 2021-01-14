# https://programmers.co.kr/learn/courses/30/lessons/12899

def solution(n):
    answer = ''

    while n > 0:

        if n % 3 == 0:
            answer = '4' + answer
            n = n // 3 - 1
        else:
            answer = str(n % 3) + answer
            n = n // 3
    return answer


print(solution(1))
print(solution(2))
print(solution(3))
print(solution(4))
