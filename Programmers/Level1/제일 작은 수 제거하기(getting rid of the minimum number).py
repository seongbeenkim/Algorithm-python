# https://programmers.co.kr/learn/courses/30/lessons/12935

def solution(arr):
    arr.remove(min(arr))
    answer = arr

    if not answer:
        answer.append(-1)

    return answer

print(solution([4, 3, 2, 1]))
print(solution([10]))
