"""

661. Image Smoother : https://leetcode.com/problems/image-smoother/

2D Matrix가 주어졌을 때, 자신을 포함한 인접한 9개의 cell의 값을 평균내어 새로운 2D Matrix를 구하는 문제
- 인접한 cell이 8개 미만인 경우에는 사용할 수 있는 모든 인접한 셀의 값의 평균을 구한다
- 구한 값의 소수점 아래는 버린다
- 주어진 matrix의 값은 [0, 255] 범위이다
- matrix의 가로, 세로의 길이는 [1, 150] 범위이다

Example:
- Input : [[1,1,1],[1,0,1],[1,1,1]]
- Output : [[0,0,0],[0,0,0],[0,0,0]]

Note:
solve() 함수를 생성하여 해결
인덱스 처리가 조금 번거로울 뿐 단순하게 해결 가능
자신을 포함한 인접 셀이 9개 미만인 경우가 있으므로 셀의 개수를 카운트하여 평균을 계산

"""

class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        self.xlen, self.ylen = len(M[0]), len(M)
        def solve(self, x: int, y: int) -> int :
            count, total = 0, 0
            for i in range(y-1 if y-1 >= 0 else y, y+2 if y+1 < self.ylen else y+1) :
                for j in range(x-1 if x-1 >= 0 else x, x+2 if x+1 < self.xlen else x+1) :
                    count += 1
                    total += M[i][j]
            return total // count
        return [[solve(self, i, j) for i in range(self.xlen)] for j in range(self.ylen)]