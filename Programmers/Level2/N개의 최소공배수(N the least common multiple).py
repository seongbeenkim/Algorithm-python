# https://programmers.co.kr/learn/courses/30/lessons/12953

def solution(arr):
    def gcd(a, b):
        if b == 0:
            return a
        else:
            return gcd(b, a % b)

    for i in range(len(arr) - 1):
        arr[i + 1] = arr[i] * arr[i + 1] // gcd(arr[i], arr[i + 1])

    return arr[-1]


print(solution([2, 6, 8, 14]))
print(solution([1, 2, 3]))
