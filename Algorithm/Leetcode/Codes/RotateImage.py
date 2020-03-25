"""

48. Rotate Image : https://leetcode.com/problems/rotate-image/

크기가 n x n인 2D matrix가 하나 주어졌을 때, 이를 시계 방향으로 90도 회전한 결과를 구하는 문제
- in-place로 해결할 것

Example:
- Input : 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
- Output :
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]

- Input : 
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]
- Output :
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]

Note:
좌상단과 우하단을 가로지르는 대각선을 기준으로 뒤집은 다음, 세로선을 기준으로 뒤집으면
90도를 회전한 것과 동일한 결과가 나온다

"""

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)) :
            for j in range(i) :
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(len(matrix)) :
            matrix[i] = matrix[i][::-1]