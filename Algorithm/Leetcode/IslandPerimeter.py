"""

463. Island Perimeter : https://leetcode.com/problems/island-perimeter/

0과 1로 이루어진 2차원 matrix가 주어졌을 때, 1로 이루어진 섬의 외곽선의 길이를 구하는 문제
- 섬은 단 하나만 존재한다
- 섬의 각 셀은 대각선으로는 이어지지 않는다
- 섬에는 호수(외부의 물과 연결되지 않는 0)가 존재하지 않는다
- 각 셀의 길이는 1이며, 주어지는 matrix의 가로와 세로 길이는 100을 넘지 않는다

Example:
- Input : [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
- Output : 16

Note:
matrix를 돌면서 1인 셀이 물과 만나는 지점의 길이를 더하는 방식으로 구현
인접한 네 개의 셀 중에 1인 셀이 있으면 그 변은 외곽선이 아님

"""

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res, width, height = 0, len(grid[0]), len(grid)
        for i in range(height) :
            for j in range(width) :
                if grid[i][j] == 1 :
                    res += 1 if i == 0 or grid[i-1][j] == 0 else 0
                    res += 1 if j == 0 or grid[i][j-1] == 0 else 0
                    res += 1 if i == height - 1 or grid[i+1][j] == 0 else 0
                    res += 1 if j == width - 1 or grid[i][j+1] == 0 else 0
        return res