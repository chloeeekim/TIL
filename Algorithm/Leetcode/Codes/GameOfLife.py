"""

289. Game of Life : https://leetcode.com/problems/game-of-life/

다음 룰을 따르는 Life 게임의 next state(generation)를 구하는 문제
- 0은 dead cell, 1은 live cell을 의미한다
- neighbors는 인접한 8개의 cell(가로, 세로, 대각선)을 의미한다
- live cell의 경우, neighbors의 live cell이 2개 미만인 경우 under-population으로 dead cell이 된다
- live cell의 경우, neighbors의 live cell이 2개 혹은 3개인 경우 그대로 유지된다
- live cell의 경우, neighbors의 live cell이 3개 초과인 경우 over-population으로 dead cell이 된다
- dead cell의 경우, neighbors의 live cell이 정확히 3개인 경우 live cell이 된다
- in-place로 구할 것

Example:
- Input : board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
- Output : [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

- Input : board = [[1,1],[1,0]]
- Output : [[1,1],[1,1]]

Note:
각 neighbors에 해당하는 위치를 tuple의 형식으로 리스트에 저장
next state는 10의 자리수, 현재 state는 1의 자리수로 변환
인접한 cell은 최대 8개이므로 count의 1의 자리수로 계산해도 문제가 발생하지 않는다
최종적으로 next state에 맞게 board를 변경

"""

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                state = board[i][j]
                count = 0
                neighbors = [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]
                for p in neighbors:
                    if p[0] >= 0 and p[0] < m and p[1] >= 0 and p[1] < n:
                        count += board[p[0]][p[1]]
                count %= 10
                if state == 0 and count == 3:
                    board[i][j] = 10
                if state == 1:
                    if count < 2 or count > 3:
                        board[i][j] = 1
                    else:
                        board[i][j] = 11
        for i in range(m):
            for j in range(n):
                if board[i][j] == 10 or board[i][j] == 11:
                    board[i][j] = 1
                else:
                    board[i][j] = 0                