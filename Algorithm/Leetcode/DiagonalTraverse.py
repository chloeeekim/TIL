"""

498. Diagonal Traverse : https://leetcode.com/problems/diagonal-traverse/

2차원 matrix가 주어졌을 때, 이를 대각선 순서로 왔다갔다하며 순회하는 문제
- matrix에 포함된 전체 숫자의 개수는 10,000개를 넘지 않는다

Example:
- Input : [[1,2,3],[4,5,6],[7,8,9]]
- Output : [1,2,4,7,5,3,6,8,9]

Note:
대각선의 방향이 오른쪽 위를 향하는 것인지 왼쪽 아래를 향하는 것인지를 isup으로 관리
matrix의 끝에 도달하면 다음으로 순회해야 할 인덱스를 찾고, 방향을 바꿔준다

"""

class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix :
            return []
        res, isup, x, y, width, height = [], True, 0, 0, len(matrix[0]), len(matrix)
        while x < width and y < height :
            res.append(matrix[y][x])
            if isup :
                x += 1
                y -= 1
                if x >= width :
                    x -= 1
                    y += 2
                    isup = False
                else :                    
                    isup = False if y < 0 else True
                    y += 1 if y < 0 else 0
            else :
                x -= 1
                y += 1
                if y >= height :
                    y -= 1
                    x += 2
                    isup = True
                else :                    
                    isup = True if x < 0 else False
                    x += 1 if x < 0 else 0
        return res