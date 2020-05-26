"""

883. Projection Area of 3D Shapes : https://leetcode.com/problems/projection-area-of-3d-shapes/

N x N grid 위에 1 x 1 x 1 짜리 큐브를 쌓아 올려서 3D shape를 만들었을 때, x, y, z 축으로 프로젝션한 면적의 합을 구하는 문제
- grid의 길이는 1 이상 50 이하이며, 가로와 세로의 길이가 동일하다
- grid[i][j]의 값은 0 이상 50 이하이다

Example:
- Input : [[2]]
- Output : 5

- Input : [[1,2],[3,4]]
- Output : 17

- Input : [[1,0],[0,2]]
- Output : 8

- Input : [[1,1,1],[1,0,1],[1,1,1]]
- Output : 14

- Input : [[2,2,2],[2,1,2],[2,2,2]]
- Output : 21

Note:
앞에서 본 것, 옆에서 본 것, 위에서 본 것의 면적을 각각 구해서 합을 구하면 된다
참고) 더 깔끔한 풀이?

"""

class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        N = len(grid)
        top = front = side = 0
        for n in range(N):
            front += max(grid[n])
            side += max(grid[i][n] for i in range(N))
            for i in range(N):
                if grid[n][i] != 0:
                    top += 1
        return top+front+side