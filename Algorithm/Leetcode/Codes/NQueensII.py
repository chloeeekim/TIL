"""

52. N-Queens II : https://leetcode.com/problems/n-queens-ii/

n이 주어졌을 때, n x n 보드에 n개의 퀸을 놓을 수 있는 가능한 가짓수를 구하는 문제
- 퀸은 서로 같은 row, column에 위치할 수 없으며, 대각선으로도 위치할 수 없다

Example:
- Input : 4
- Output : 2

Note:
nqueen() 함수를 생성하여 recursive하게 해결
리스트에는 idx번째 row의 queen의 인덱스를 저장
이전 row들의 queen의 위치를 비교하여 같은 column에 위치하거나 대각선에 위치한 경우는 valid하지 않는 경우

"""

class Solution:
    def totalNQueens(self, n: int) -> int:
        self.count, arr, self.length = 0, [-1 for _ in range(n)], n
        def nqueen(self, tmp: list, idx: int) -> bool :
            if idx == self.length :
                self.count += 1
                return True
            for i in range(self.length) :
                isvalid = True
                for j in range(idx) :
                    if tmp[j] == i : 
                        isvalid = False
                        break
                    if abs(i - tmp[j]) == idx - j :
                        isvalid = False
                        break
                if isvalid :
                    tmp[idx] = i
                    nqueen(self, tmp[:], idx + 1)
        nqueen(self, arr, 0)
        return self.count