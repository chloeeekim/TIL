"""

1037. Valid Boomerang : https://leetcode.com/problems/valid-boomerang/

세 개의 포인트가 주어졌을 때, 이 포인트들이 boomerang인지 확인하는 문제
- boomerang은 모두 다른 포인트들이 하나의 직선 위에 존재하지 않는 경우를 의미한다

Example:
- Input : points = [[1,1],[2,3],[3,2]]
- Output : true

- Input : points = [[1,1],[2,2],[3,3]]
- Output : false

- Input : points = [[0,0],[1,1],[1,1]]
- Output : false

Note:
기울기를 구하는 함수를 생성하여 세 포인트 사이의 기울기 세 개를 확인
기울기 셋이 모두 다른 경우 조건을 만족하므로 set을 사용하여 겹치는 내용을 확인

"""

class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        def getSlope(x1, y1, x2, y2):
            return (y2-y1) / (x2-x1) if x2-x1 != 0 else float('inf')
        slopes = [getSlope(*points[0], *points[1]), getSlope(*points[1], *points[2]), getSlope(*points[0], *points[2])]
        return len(set(slopes)) == 3