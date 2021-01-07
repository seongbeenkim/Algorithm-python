# https://programmers.co.kr/learn/courses/30/lessons/12943

def solution(num):
    answer = 0

    while num != 1:
        if num % 2 == 0:
            num //= 2
        else:
            num *= 3
            num += 1
        answer += 1

        if answer > 500:
            return -1
    return answer

print(solution(6))
print(solution(16))
print(solution(626331))
