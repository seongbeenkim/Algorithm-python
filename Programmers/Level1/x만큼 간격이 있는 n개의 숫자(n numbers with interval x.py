# https://programmers.co.kr/learn/courses/30/lessons/12954

def solution(x, n):

    if x == 0:
        return [0] * n

    if x < 0:
        answer = [i for i in range(x * n, x + 1, -x)]
        answer.sort(reverse=True)
    else:
        answer = [i for i in range(x * n, x - 1, -x)]
        answer.sort()

    return answer

print(solution(2, 5))
print(solution(4, 3))
print(solution(-4, 2))
