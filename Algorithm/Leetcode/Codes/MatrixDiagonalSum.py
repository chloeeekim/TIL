"""

1572. Matrix Diagonal Sum : https://leetcode.com/problems/matrix-diagonal-sum/

정사각형 모양의 matrix mat이 주어졌을 때, 대각선의 합을 구하는 문제
- 대각선의 겹치는 부분은 한 번만 계산한다
- matrix의 길이 n은 1 이상 100 이하이다
- matrix 내의 값은 1 이상 100 이하이다

Example:
- Input : mat = [[1,2,3],[4,5,6],[7,8,9]]
- Output : 25
- 1+5+9+3+7=25로, 가운데 5는 겹치는 부분이므로 한 번만 계산한다

- Input : mat = [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]
- Output : 8

- Input : [[5]]
- Output : 5

Note:
대각선에 위치한 값을 하나씩 더하되,
한 번 계산한 값은 0으로 변경하여 두 번 더해지지 않도록 하는 방식

"""

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total, length = 0, len(mat)
        for i in range(length):
            total += mat[i][i]
            mat[i][i] = 0
            total += mat[length-i-1][i]
            mat[length-i-1][i] = 0
        return total