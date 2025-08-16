"""

1차 / 프렌즈4블록 : https://school.programmers.co.kr/learn/courses/30/lessons/17679

2차원 배열 형태로 블록 배치가 주어졌을 때, 같은 블록이 2x2 형태로 붙어있을 경우 사라질 때, 최종적으로 지워지는 블록의 개수를 구하는 문제
- 같은 블록은 여러 2x2에 포함될 수 있으며, 지워지는 조건에 만족하는 2x2 모양이 여러 개 있다면 한꺼번에 지워진다
- 블록이 지워진 후에는 위에 있는 블록이 아래로 떨어져 빈 공간을 채운다
- 빈 공간을 채운 뒤에 다시 2x2 형태로 같은 블록이 모이면 다시 지워지고 떨어지고를 반복한다
- board는 길이 n인 문자열 m개의 배열로 주어진다
- 블록을 나타내는 문자는 대문자 A에서 Z가 사용된다

Example:
- Input : m=4, n=5, board=["CCBDE", "AAADE", "AAABF", "CCBBF"]
- Output : 14

- Input : m=6, n=6, board=["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]
- Output : 15

Note:
블록이 사라진 자리에 떨어지는 기능을 문자열에서 '0'을 지우고 zfill로 왼쪽에 패딩하는 방식으로 구현
변환을 편리하게 하기 위해 board를 90도 회전

"""

import copy

def solution(m, n, board):
    total = 0
    square = [[0, 0], [0, 1], [1, 0], [1, 1]]
    board = [list(row) for row in zip(*board)]

    while True:
        temp = copy.deepcopy(board)
        changed = False
        for i in range(n-1):
            for j in range(m-1):
                if len(set(board[i+dx][j+dy] for dx, dy in square)) == 1 and board[i][j] != "0":
                    changed = True
                    for dx, dy in square:
                        temp[i+dx][j+dy] = "0"
        if changed:
            for i in range(n):
                temp[i] = list("".join(temp[i]).replace("0", "").zfill(m))
            board = copy.deepcopy(temp)
        else:
            break

    return sum(ch == '0' for row in board for ch in row)