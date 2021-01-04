# https://programmers.co.kr/learn/courses/30/lessons/12903

def solution(arr):
    answer = []
    for i, number in enumerate(arr):
        if i == 0:
            answer.append(number)
            continue

        if arr[i - 1] != arr[i]:
            answer.append(number)

    return answer


print(solution([1, 1, 3, 3, 0, 1, 1]))
print(solution([4, 4, 4, 3, 3]))
