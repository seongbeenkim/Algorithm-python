# https://programmers.co.kr/learn/courses/30/lessons/12950

def solution(arr1, arr2):
    n = len(arr1)
    m = len(arr1[0])

    answer = [[arr1[i][j] + arr2[i][j] for j in range(m)] for i in range(n)]
    return answer


print(solution([[1, 2], [2, 3]], [[3, 4], [5, 6]]))
print(solution([[1], [2]], [[3], [4]]))
