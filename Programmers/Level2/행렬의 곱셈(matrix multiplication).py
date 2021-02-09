# https://programmers.co.kr/learn/courses/30/lessons/12949

def solution(arr1, arr2):
    answer = []
    a = len(arr1)
    b = len(arr1[0])
    c = len(arr2[0])

    for i in range(a):
        row = []
        for j in range(c):
            temp = 0
            for k in range(b):
                temp += arr1[i][k] * arr2[k][j]
            row.append(temp)
        answer.append(row)

    return answer


print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))
print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))
