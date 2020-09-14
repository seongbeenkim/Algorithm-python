#https://www.welcomekakao.com/learn/courses/30/lessons/43165

def dfs(index, res, numbers, target):
    if index == len(numbers):
        if res == target:
            return 1
        else:
            return 0
    cnt = 0
    cnt += dfs(index + 1, numbers[index] + res, numbers, target)
    cnt += dfs(index + 1, res - numbers[index], numbers, target)
    return cnt


def solution(numbers, target):
    answer = dfs(0, 0, numbers, target)
    return answer

print(solution([1, 1, 1, 1, 1],3))