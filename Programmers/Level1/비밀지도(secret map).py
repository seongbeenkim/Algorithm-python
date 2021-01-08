# https://programmers.co.kr/learn/courses/30/lessons/17681

def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        result = arr1[i] | arr2[i]
        temp = ""

        for j in range(n - 1, -1, -1):
            if result - (2 ** j) >= 0:
                temp += "#"
                result -= 2 ** j
            else:
                temp += " "

        answer.append(temp)
    return answer


print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
print(solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]))
