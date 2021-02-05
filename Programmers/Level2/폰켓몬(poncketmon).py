# https://programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    n = len(nums) // 2
    nums = set(nums)

    if len(nums) >= n:
        return n
    else:
        return len(nums)


print(solution([3, 1, 2, 3]))
print(solution([3, 3, 3, 2, 2, 4]))
print(solution([3, 3, 3, 2, 2, 2]))
