# https://programmers.co.kr/learn/courses/30/lessons/12905

def solution(board):
    n = len(board)
    m = len(board[0])

    for x in range(1, n):
        for y in range(1, m):
            if board[x][y] == 1:
                board[x][y] = min(board[x - 1][y - 1], min(board[x - 1][y], board[x][y - 1])) + 1
    answer = []
    for i in range(n):
        answer.append(max(board[i]))
    return max(answer) ** 2


print(solution([[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]))
print(solution([[0, 0, 1, 1], [1, 1, 1, 1]]))
