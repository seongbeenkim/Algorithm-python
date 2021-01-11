# https://programmers.co.kr/learn/courses/30/lessons/64061

def solution(board, moves):
    answer = 0
    box = []
    n = len(board)

    for j in moves:
        j -= 1
        for i in range(n):
            if board[i][j] == 0:
                continue

            box.append(board[i][j])
            board[i][j] = 0

            if len(box) > 1 and box[-1] == box[-2]:
                answer += 2
                del box[-2]
                del box[-1]

            break

    return answer


print(solution([[0, 0, 0, 0, 0],
                [0, 0, 1, 0, 3],
                [0, 2, 5, 0, 1],
                [4, 2, 4, 4, 2],
                [3, 5, 1, 3, 1]],
               [1, 5, 3, 5, 1, 2, 1, 4]))
