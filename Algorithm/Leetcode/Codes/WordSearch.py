"""

79. Word Search : https://leetcode.com/problems/word-search/

알파벳으로 이루어진 2D matrix가 주어졌을 때, 주어지는 word가 존재하는지 확인하는 문제
- word는 인접한 letter들의 연결로 이루어진다 (대각선으로는 연결되지 않는다)
- 주어지는 문자들은 모두 영문 알파벳이다

Example:
- Input : word = "ABCCED", board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
- Output : true

- Input : word = "SEE", board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
- Output : true

- Input : word = "ABCB", board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
- Output : false

Note:
solve() 함수를 생성하여 recursive하게 해결
다음 칸으로 이동할 수 있는지 확인 후 DFS 방식으로 matrix를 순회
참고) 더 효율적인 방법?

"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def solve(self, x: int, y: int, remain: str, seen: List[List[int]]) -> bool:
            if not remain :
                return True
            res = False
            if x-1 >= 0 and [x-1, y] not in seen and board[x-1][y] == remain[0] :                
                res = res or solve(self, x-1, y, remain[1:], seen + [[x-1, y]])
            if y-1 >= 0 and [x, y-1] not in seen and board[x][y-1] == remain[0] :
                res = res or solve(self, x, y-1, remain[1:], seen + [[x, y-1]])
            if x+1 < len(board) and [x+1, y] not in seen and board[x+1][y] == remain[0] :
                res = res or solve(self, x+1, y, remain[1:], seen + [[x+1, y]])
            if y+1 < len(board[0]) and [x, y+1] not in seen and board[x][y+1] == remain[0] :
                res = res or solve(self, x, y+1, remain[1:], seen + [[x, y+1]])
            return res
        res = False
        for i in range(len(board)) :
            for j in range(len(board[0])) :
                if board[i][j] == word[0] :
                    res = res or solve(self, i, j, word[1:], [[i, j]])
                    if res :
                        return True
        return res