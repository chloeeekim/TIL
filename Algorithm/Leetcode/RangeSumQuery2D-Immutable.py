"""

304. Range Sum Query 2D - Immutable : https://leetcode.com/problems/range-sum-query-2d-immutable/

숫자가 포함된 2D matrix가 주어졌을 때, 특정 사각형 범위 내의 합을 구하는 문제
- 사각형의 왼쪽 위(row1, col1) 지점과 오른쪽 아래(row2, col2) 지점의 값이 주어진다
- 입력된 matrix는 변경되지 않는다
- sumRegion 함수는 여러 번 호출될 수 있다
- row1 <= row2, col1 <= col2 라고 가정해도 좋다

Example:
- Input : ["NumMatrix","sumRegion","sumRegion","sumRegion"]
[[[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]],[2,1,4,3],[1,1,2,2],[1,2,2,4]]
- Output : [null,8,11,12]
- sumRegion(2,1,4,3) -> 8 / sumRegion(1,1,2,2) -> 11 / sumRegion(1,2,2,4) -> 12

Note:
sumRegion 요청이 들어올 때마다 합을 구하는 것은 비효율적
matrix의 순서나 값이 변경되지 않고, 특정 범위의 합만 구하면 되므로
sums matrix를 생성하여 (0,0)부터 해당 지점까지의 합을 저장
(row1, col1, row2, col2)의 범위의 합을 구하려면 (row2, col2)까지의 합에
(row2-1, col1), (row1, col2-1)까지의 합을 뺀 다음
두 번 빠지게 되는 (row1-1, col1-1)까지의 합을 더해주면 된다
여기서는 첫 번째 열과 행에 0의 값이 들어가 있으므로 인덱스를 1씩 더해서 계산

"""

class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        if not matrix :
            self.sums = []
            return
        self.sums = [[0 for _ in range(len(matrix[0]) + 1)] for _ in range(len(matrix) + 1)]
        for i in range(len(matrix)) :
            for j in range(len(matrix[0])) :
                self.sums[i+1][j+1] = matrix[i][j] + self.sums[i+1][j] + self.sums[i][j+1] - self.sums[i][j]
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.sums[row2+1][col2+1] - self.sums[row2+1][col1] - self.sums[row1][col2+1] + self.sums[row1][col1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)