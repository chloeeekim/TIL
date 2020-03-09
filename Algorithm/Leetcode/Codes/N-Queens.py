"""

51. N-Queens : https://leetcode.com/problems/n-queens-/

n이 주어졌을 때, n x n 보드에 n개의 퀸을 놓을 수 있는 가능한 경우의 수를 구하는 문제
- 퀸은 서로 같은 row, column에 위치할 수 없으며, 대각선으로도 위치할 수 없다
- 빈 칸은 '.'로, 퀸은 'Q'로 표시한다

Example:
- Input : 4
- Output : [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]

Note:
nqueen() 함수를 생성하여 recursive하게 해결
리스트에는 idx번째 row의 queen의 인덱스를 저장
이전 row들의 queen의 위치를 비교하여 같은 column에 위치하거나 대각선에 위치한 경우는 valid하지 않는 경우
n번째 퀸까지 valid하게 놓인 경우 출력 스타일과 동일하게 변경하여 결과 리스트에 저장

"""

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res, arr, self.length = [], [-1 for _ in range(n)], n
        def nqueen(self, tmp: list, idx: int) -> bool :
            if idx == self.length :
                sol = []
                for row in tmp :
                    str = "." * row + "Q" + "." * (self.length - row - 1)
                    sol.append(str)
                res.append(sol)
                return True
            for i in range(self.length) :
                isvalid = True
                for j in range(idx) :
                    if tmp[j] == i :
                        isvalid = False
                        break
                    elif abs(i - tmp[j]) == idx - j :
                        isvalid = False
                        break
                if isvalid :
                    tmp[idx] = i
                    nqueen(self, tmp[:], idx + 1)
            return False
        nqueen(self, arr, 0)
        return res