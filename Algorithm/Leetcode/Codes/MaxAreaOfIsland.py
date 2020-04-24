"""

695. Max Area of Island : https://leetcode.com/problems/max-area-of-island/

0과 1로 이루어진 2D grid가 주어졌을 때, 1로 이루어진 섬의 최대 면적을 구하는 문제
- 섬은 4-directionally connected되어 있다 (대각선으로 연결되지 않는다)
- 주어진 grid의 네 끝은 전부 물로 이루어진다고 가정한다

Example:
- Input : 
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
- Output : 6

- Input : [[0,0,0,0,0,0,0,0]]
- Output : 0

Note:
getArea() 함수를 생성하여 recursive하게 해결
확인한 위치는 중복해서 확인하지 않도록 0으로 변경
네 방향으로 섬이 연결되는지 확인하여 해당 섬의 전체 면적을 확인

"""

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.width, self.height = len(grid[0]), len(grid)
        def getArea(self, x: int, y: int) -> int:
            total = 1
            grid[x][y] = 0
            total += getArea(self, x-1, y) if x > 0 and grid[x-1][y] == 1 else 0
            total += getArea(self, x, y-1) if y > 0 and grid[x][y-1] == 1 else 0
            total += getArea(self, x+1, y) if x < self.height-1 and grid[x+1][y] == 1 else 0
            total += getArea(self, x, y+1) if y < self.width-1 and grid[x][y+1] == 1 else 0
            return total
        res = 0
        for i in range(self.height):
            for j in range(self.width):
                if grid[i][j] == 1:
                    area = getArea(self, i, j)
                    res = max(res, area)
        return res