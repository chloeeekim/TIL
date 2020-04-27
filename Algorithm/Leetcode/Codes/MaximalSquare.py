"""

221. Maximal Square : https://leetcode.com/problems/maximal-square/

0과 1로 이루어진 2D binary matrix가 주어졌을 때, 1로 만들 수 있는 정사각형의 최대 크기를 구하는 문제

Example:
- Input :
[["1","0","1","0","0"],
 ["1","0","1","1","1"],
 ["1","1","1","1","1"],
 ["1","0","0","1","0"]]
- Output : 4

Note:
dp로 해결
arr에는 해당 인덱스를 포함하여 좌상단 방향으로 만들 수 있는 정사각형의 최대 길이를 저장

"""

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        width, height = len(matrix[0]), len(matrix)
        arr = [[0 for _ in range(width+1)] for _ in range(height+1)]
        for i in range(1, height+1):
            for j in range(1, width+1):
                if matrix[i-1][j-1] == '0':
                    continue
                arr[i][j] = min(arr[i-1][j], arr[i][j-1], arr[i-1][j-1])+1
        return max(max(row) for row in arr) ** 2