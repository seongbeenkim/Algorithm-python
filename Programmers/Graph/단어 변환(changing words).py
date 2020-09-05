#https://programmers.co.kr/learn/courses/30/lessons/43163

def dfs(index, count, begin, target, words, check):
    ans = 51

    if target == begin:
        return count

    if index == len(words):
        return 51

    for i in range(len(words)):
        if not check[i]:
            diff = 0
            for j in range(len(target)):
                if words[i][j] != begin[j]:
                    diff += 1
            if diff == 1:
                check[i] = True
                first = dfs(index + 1, count + 1, words[i], target, words, check)
                ans = min(first, ans)
                check[i] = False
    return ans


def solution(begin, target, words):
    answer = 0
    check = [False] * len(words)

    temp = dfs(0, 0, begin, target, words, check)

    if temp != 51:
        answer = temp
    return answer

print(solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"]))