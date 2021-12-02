"""

836. Rectangle Overlap : https://leetcode.com/problems/rectangle-overlap/

두 개의 사각형의 포인트가 주어졌을 때, 두 사각형이 겹쳐져 있는지 확인하는 문제
- 두 사각형은 영역이 0이 아닌 유효한 사각형이다

Example:
- Input : rec1 = [0,0,2,2], rec2 = [1,1,3,3]
- Output : true

- Input : rec1 = [0,0,1,1], rec2 = [1,0,2,1]
- Output : False

- Input : rec1 = [0,0,1,1], rec2 = [2,2,3,3]
- Output : false

Note:
두 선분이 겹쳐질 수 있는지 판별하는 check 함수를 생성
상하 선분과 좌우 선분이 모두 겹쳐지는 경우 두 사각형이 겹쳐진다

"""

class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        def check(left1, right1, left2, right2):
            return min(right1, right2) > max(left1, left2)
        return (check(rec1[0], rec1[2], rec2[0], rec2[2]) and (check(rec1[1], rec1[3], rec2[1], rec2[3])))