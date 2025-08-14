"""

[PCCE 기출문제] 9번 / 이웃한 칸 : https://school.programmers.co.kr/learn/courses/30/lessons/250125

각 칸마다 색이 칠해진 2차원 배열에서 한 칸을 골랐을 때, 인접한 칸 중 같은 색깔로 칠해진 칸의 개수를 구하는 문제
- board의 길이와 board[n]의 길이는 동일하다
- board[h][w]는 영어 소문자로만 이루어져 있다

Example:
- Input : board=
[
    ["blue", "red", "orange", "red"],
    ["red", "red", "blue", "orange"],
    ["blue", "orange", "red", "red"],
    ["orange", "orange", "red", "blue"]
], h=1, w=1
- Output : 2

- Input : board=
[
    ["yellow", "green", "blue"],
    ["blue", "green", "yellow"],
    ["yellow", "blue", "blue"]
], h=0, w=1
- Output : 1

Note:
문제 지문에 주어진 과정을 그대로 구현

"""

def solution(board, h, w):
    n = len(board)
    count = 0
    dh, dw = [0, 1, -1, 0], [1, 0, 0, -1]
    for i in range(len(dh)):
        h_check, w_check = h+dh[i], w+dw[i]
        if (0 <= h_check < n and 0 <= w_check < n):
            if (board[h][w] == board[h_check][w_check]):
                count += 1
    return count