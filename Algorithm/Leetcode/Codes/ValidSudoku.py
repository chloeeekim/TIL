"""

36. Valid Sudoku : https://leetcode.com/problems/valid-sudoku/

9x9 스도쿠 board가 주어졌을 때, 해당 스도쿠가 valid한지 확인하는 문제
- 각 row에는 1부터 9까지의 숫자가 중복 없이 포함되어야 한다
- 각 column에는 1부터 9까지의 숫자가 중복 없이 포함되어야 한다
- 총 9개의 3x3짜리 sub-box에는 1부터 9까지의 숫자가 중복 없이 포함되어야 한다
- 비어 있는 cell은 '.'으로 나타낸다

Example:
- Input :
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
- Output : true

- Input : 
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
- Output : false
- 첫 번째 column과 첫 번째 sub-box에서 8이 중복

Note:
단순 반복으로 중복을 확인하는 방식
각 column, row별로 우선 확인하고, 3x3 sub-box별로 확인을 진행

"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9) :
            row, col = set(), set()
            for j in range(9) :
                if board[i][j] not in row :
                    row.add(board[i][j] if board[i][j] != '.' else None)
                else :
                    return False
                if board[j][i] not in col :
                    col.add(board[j][i] if board[j][i] != '.' else None)
                else :
                    return False
        for x in range(0, 9, 3) :
            for y in range(0, 9, 3) :                
                seen = set()
                for i in range(3) :
                    for j in range(3) :
                        if board[x+i][y+j] not in seen :
                            seen.add(board[x+i][y+j] if board[x+i][y+j] != '.' else None)
                        else :
                            return False
        return True