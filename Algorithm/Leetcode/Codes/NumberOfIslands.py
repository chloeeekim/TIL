"""

200. Number of Islands : https://leetcode.com/problems/number-of-islands/

0과 1로 구성된 2d grid map이 주어졌을 때, 1로 이루어진 섬의 개수를 찾는 문제
- 하나의 섬은 horizontally 혹은 vertically하게 연결되어 있다 (대각선은 포함되지 않는다)
- grid의 외곽은 전부 물로 뒤덮여있다고 가정한다

Example:
- Input : [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
- Output : 1

- Input : [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
- Output : 3

Note:
island() 함수를 생성하여 recursive하게 해결
grid를 순회하다 1을 발견하면 해당 위치로부터 recursive하게 주변을 탐색하여 섬을 찾는 방법
이미 순회한 곳은 0으로 변경하여 중복되는 일이 없도록 함

"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        def island(self, x: int, y: int) :
            grid[x][y] = '0'
            if x > 0 and grid[x-1][y] == '1' :
                island(self, x-1, y)
            if x < len(grid) - 1 and grid[x+1][y] == '1' :
                island(self, x+1, y)
            if y > 0 and grid[x][y-1] == '1' :
                island(self, x, y-1)
            if y < len(grid[0]) - 1 and grid[x][y+1] == '1' :
                island(self, x, y+1)
        for i in range(len(grid)) :
            for j in range(len(grid[0])) :
                if grid[i][j] == '1' :
                    island(self, i, j)
                    count += 1
        return count