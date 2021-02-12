# https://programmers.co.kr/learn/courses/30/lessons/68936

def solution(arr):
    answer = [0, 0]
    n = len(arr)
    m = len(arr[0])

    def count(x, y, d):
        zero_count = 0
        one_count = 0

        for i in range(x, x + d):
            for j in range(y, y + d):
                if arr[i][j] == 0:
                    zero_count += 1
                else:
                    one_count += 1

        if zero_count == 0:
            answer[1] += 1
            return True
        elif one_count == 0:
            answer[0] += 1
            return True

        elif zero_count != 0 and one_count != 0:
            if d == 2:
                answer[0] += zero_count
                answer[1] += one_count
                return True
            else:
                return False

    def go(sx, sy, ex, ey, d):

        for i in range(sx, ex, d):
            for j in range(sy, ey, d):
                if not count(i, j, d):
                    go(i, j, i + d, j + d, d // 2)

    go(0, 0, n, m, n // 2)

    if answer[0] == 0:
        answer[1] = 1
    elif answer[1] == 0:
        answer[0] = 1

    return answer


print(solution([[1, 1, 0, 0],
                [1, 0, 0, 0],
                [1, 0, 0, 1],
                [1, 1, 1, 1]]))

print(solution([[1, 1, 1, 1, 1, 1, 1, 1],
                [0, 1, 1, 1, 1, 1, 1, 1],
                [0, 0, 0, 0, 1, 1, 1, 1],
                [0, 1, 0, 0, 1, 1, 1, 1],
                [0, 0, 0, 0, 0, 0, 1, 1],
                [0, 0, 0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 1, 0, 0, 1],
                [0, 0, 0, 0, 1, 1, 1, 1]]))
