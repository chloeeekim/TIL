"""

766. Toeplitz Matrix : https://leetcode.com/problems/toeplitz-matrix/

주어진 matrix가 toeplitz인지 확인하는 문제
- toeplitz: 좌상단에서 우하단으로 이어지는 모든 대각선이 동일한 값으로 이루어지는 것
- matrix의 row와 column은 [1,20] 범위이다
- matrix[i][j]는 [0,99]까지의 정수이다

Example:
- Input : matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
- Output : True
- [9], [5,5], [1,1,1], [2,2,2], [3,3], [4]

- Input : matrix = [[1,2],[2,2]]
- Output : False
- [1,2]이므로 다른 값으로 이루어져 있다

Note:
첫 번째 row와 첫 번째 column은 이전 값이 없으므로 확인할 필요가 없음
두 번째 row와 column부터 좌상단 대각선에 위치한 값과 비교하여 다른 경우 toeplitz가 아님

"""

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(1, len(matrix)) :
            for j in range(1, len(matrix[0])) :
                if matrix[i-1][j-1] != matrix[i][j] :
                    return False
        return True