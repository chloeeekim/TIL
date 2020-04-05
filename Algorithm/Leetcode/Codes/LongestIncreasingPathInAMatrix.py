"""

329. Longest Increasing Path in a Matrix : https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

정수가 포함된 2x2 matrix가 주어졌을 때, 가장 긴 증가수열 path의 길이를 구하는 문제
- 각 셀에서 상하좌우로만 이동할 수 있다 (대각선으로 이동할 수 없다)
- matrix의 바깥으로 벗어나 이동할 수 없다

Example:
- Input : nums = 
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
] 
- Output : 4
- longest increasing path = [1,2,6,9]

- Input : nums = 
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
] 
- Output : 4
- longest increasing path = [3,4,5,6]

Note:
해당 위치에서 시작하는 최대 증가수열 path의 길이를 저장하는 방식 (dp)
findPath() 함수를 생성하여 recursive하게 해결
이전에 확인한 위치라면 arr에 저장되어 있으므로 그 이상 확인할 필요가 없다

"""

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        arr = [[-1 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        res = 0
        def findPath(x: int, y: int, count: int) -> int:
            if arr[x][y] != -1:
                return arr[x][y]
            ncount = 0
            if x > 0 and matrix[x-1][y] > matrix[x][y]:
                ncount = max(ncount, findPath(x-1, y, count+1))
            if y > 0 and matrix[x][y-1] > matrix[x][y]:
                ncount = max(ncount, findPath(x, y-1, count+1))
            if x < len(matrix)-1 and matrix[x+1][y] > matrix[x][y]:
                ncount = max(ncount, findPath(x+1, y, count+1))
            if y < len(matrix[0])-1 and matrix[x][y+1] > matrix[x][y]:
                ncount = max(ncount, findPath(x, y+1, count+1))
            arr[x][y] = ncount + 1
            return ncount + 1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                arr[i][j] = findPath(i, j, 0)
                res = max(res, arr[i][j])
        return res