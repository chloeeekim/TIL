"""

733. Flood Fill : https://leetcode.com/problems/flood-fill/

2D matrix와 시작 인덱스가 주어졌을 때, 새로운 컬러로 flood fill하는 문제
- 주어진 matrix에는 0부터 65535까지의 숫자가 포함된다
- flood fill은 4-directionally connected한 셀만 고려한다

Example:
- Input : image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2
- Output : [[2,2,2],[2,2,0],[2,0,1]]

Note:
solve() 함수를 생성하여 recursive하게 해결
컬러가 시작 인덱스의 첫 컬러와 동일한지 확인하며 네 방향으로 확장

"""

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        old, width, height = image[sr][sc], len(image[0]), len(image)
        if old == newColor:
            return image
        def solve(x: int, y: int):
            image[x][y] = newColor
            if x > 0 and image[x-1][y] == old:
                solve(x-1, y)
            if y > 0 and image[x][y-1] == old:
                solve(x, y-1)
            if x < height-1 and image[x+1][y] == old:
                solve(x+1, y)
            if y < width-1 and image[x][y+1] == old:
                solve(x, y+1)
        solve(sr, sc)
        return image