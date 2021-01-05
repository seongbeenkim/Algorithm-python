#https://programmers.co.kr/learn/courses/30/lessons/12932

def solution(n):
    answer = []
    while n > 0:
        k = n % 10
        answer.append(k)
        n //= 10

    return answer

print(solution(12345))