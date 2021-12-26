"""

973. K closest Points to Origin : https://leetcode.com/problems/k-closest-points-to-origin/

포인트들이 주어졌을 때, 원점에서 가장 가까운 k개를 리턴하는 문제
- 결과는 어떠한 순서로 리턴해도 상관 없다

Example:
- Input : points = [[1,3],[-2,2]], k = 1
- Output : [[-2,2]]

- Input : points = [[3,3],[5,-1],[-2,4]], k = 2
- Output : [[3,3],[-2,4]]

Note:
원점으로부터의 거리는 sqrt(x**2+y**2)이지만 sqrt까지 할 필요 없음
lambda를 사용하여 정렬

"""

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda p: p[0]**2 + p[1]**2)
        return points[:k]