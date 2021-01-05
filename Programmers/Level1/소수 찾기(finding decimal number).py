# https://programmers.co.kr/learn/courses/30/lessons/12921

def solution(n):
    answer = 0
    check = [True] * (n + 1)

    for i in range(2, n + 1):
        if check[i] == True:
            check[i] = False
            answer += 1

        k = i * i

        while k <= n:
            check[k] = False
            k += i

    return answer


print(solution(10))
print(solution(5))
