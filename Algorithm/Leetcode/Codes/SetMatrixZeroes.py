"""

73. Set Matrix Zeroes : https://leetcode.com/problems/set-matrix-zeroes/

주어진 m x n matrix에서 0이 있을 때, 그 row와 column을 전부 0으로 만드는 문제
- in-place로 해결해야 한다

Example:
- Input : [[1,1,1],[1,0,1],[1,1,1]]
- Output : [[1,0,1],[0,0,0],[1,0,1]]

- Input : [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
- Output : [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

Note:
0으로 만들어야 하는 row와 column을 확인 후 한꺼번에 0으로 변환하는 방법
유일성을 유지하기 위해 set을 사용

"""

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix[0]), len(matrix)
        rows, cols = set(), set()
        for i in range(n) :
            for j in range(m) :
                if matrix[i][j] == 0 :
                    rows.add(j)
                    cols.add(i)
        for j in rows :
            for i in range(n) :
                matrix[i][j] = 0
        for i in cols :
            for j in range(m) :
                matrix[i][j] = 0