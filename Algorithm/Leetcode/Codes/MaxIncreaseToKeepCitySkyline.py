"""

807. Max Increase to Keep City Skyline : https://leetcode.com/problems/max-increase-to-keep-city-skyline/

각 위치의 빌딩의 높이가 포함된 2D array가 주어졌을 때, skyline에 영향을 받지 않는 선에서 빌딩의 높이를 최대로 높였을 때 추가되는 높이의 합을 구하는 문제
- height가 0인 경우에도 빌딩으로 간주한다
- grid의 너비나 높이는 50을 넘지 않는다
- grid에 포함된 모든 빌딩의 높이는 [0, 100] 범위이다

Example:
- Input :
[[3,0,8,4],
 [2,4,5,7],
 [9,2,6,3],
 [0,3,1,0]]
- Output : 35
- 위나 아래에서 본 skyline = [9, 4, 8, 7], 옆에서 본 skyline = [8, 7, 9, 3]
- skyline에 영향을 받지 않게 높이를 높인 grid = [[8,4,8,7],[7,4,7,7],[9,4,8,7],[3,3,3,3]]


Note:
skyline은 각 row, col 별로 빌딩의 최대 높이이며,
각 위치의 새로운 빌딩의 높이는 min(위에서 본 높이, 옆에서 본 높이)가 된다

"""

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        width, height = len(grid[0]), len(grid)
        cols = [max([x for x in grid[y]]) for y in range(height)]
        rows = [max([grid[x][y] for x in range(height)]) for y in range(width)]
        total = 0
        for i in range(height):
            for j in range(width):
                newh = min(cols[i], rows[j])
                total += newh-grid[i][j]
        return total