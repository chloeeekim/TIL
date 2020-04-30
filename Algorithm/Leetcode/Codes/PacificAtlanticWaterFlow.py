"""

417. Pacific Atlantic Water Flow : https://leetcode.com/problems/pacific-atlantic-water-flow/

m x n matrix가 주어졌을 때, pacific ocean과 atlantic ocean에 둘 다 도달할 수 있는 지점을 모두 찾는 문제
- pacific ocean은 왼쪽과 위쪽 edge에, atlantic ocean은 오른쪽과 아래쪽 edge에 닿아 있다
- 물은 네 방향으로만 흐른다 (대각선으로 흐르지 않는다)
- 물은 높은 곳에서 낮은 곳으로 흐르거나 같은 곳으로만 흐른다
- m과 n은 150 이하이다

Example:
- Input : 
[[1,2,2,3,5],
 [3,2,3,4,4],
 [2,4,5,3,1],
 [6,7,1,4,5],
 [5,1,1,2,4]]
- Output : [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

Note:
canFlow() 함수를 생성하여 recursive하게 해결
pacific 혹은 atlatic ocean에 도달할 수 있는지를 각 matrix에 따로 저장하는 방식
두 matrix에서 둘 다 1인 경우(도달할 수 있는 경우) 결과 list에 추가
참고) 더 깔끔한 방식?

"""

class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return []
        self.width, self.height = len(matrix[0]), len(matrix)
        pacific, atlantic = [[0]*self.width for _ in range(self.height)], [[0]*self.width for _ in range(self.height)]
        def canFlow(self, x: int, y: int, arr: List[List[int]]):
            if arr[x][y] == 1:
                return
            arr[x][y] = 1
            if x > 0 and matrix[x-1][y] >= matrix[x][y]:
                canFlow(self, x-1, y, arr)
            if y > 0 and matrix[x][y-1] >= matrix[x][y]:
                canFlow(self, x, y-1, arr)
            if x < self.height-1 and matrix[x+1][y] >= matrix[x][y]:
                canFlow(self, x+1, y, arr)
            if y < self.width-1 and matrix[x][y+1] >= matrix[x][y]:
                canFlow(self, x, y+1, arr)
        for i in range(self.height):
            canFlow(self, i, 0, pacific)
            canFlow(self, i, self.width-1, atlantic)
            for j in range(self.width):
                if i == 0:
                    canFlow(self, i, j, pacific)
                if i == self.height-1:
                    canFlow(self, i, j, atlantic)
        res = []
        for i in range(self.height):
            for j in range(self.width):
                if pacific[i][j] == 1 and atlantic[i][j] == 1:
                    res.append([i, j])
        return res