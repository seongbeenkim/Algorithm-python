# https://programmers.co.kr/learn/courses/30/lessons/12910

def solution(arr, divisor):
    answer = []
    for number in arr:
        if number % divisor == 0:
            answer.append(number)

    if len(answer) == 0:
        return [-1]

    answer.sort()
    return answer


print(solution([5, 9, 7, 10], 5))
print(solution([2, 36, 1, 3], 1))
print(solution([3, 2, 6], 10))
