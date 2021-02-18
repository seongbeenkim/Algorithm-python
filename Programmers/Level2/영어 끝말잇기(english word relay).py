# https://programmers.co.kr/learn/courses/30/lessons/12981

def solution(n, words):
    answer = [0, 0]
    saved_words = set()
    saved_words.add(words[0])
    last_word = words[0]

    for i in range(1, len(words)):
        if last_word[-1] != words[i][0] or words[i] in saved_words:
            answer[0] = (i % n) + 1
            answer[1] = (i // n) + 1
            break

        saved_words.add(words[i])
        last_word = words[i]

    return answer


print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))
