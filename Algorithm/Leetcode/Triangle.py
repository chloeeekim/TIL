"""

120. Triangle : https://leetcode.com/problems/triangle/

삼각형 형태의 2차원 배열(리스트)이 주어졌을 때, top에서 bottom까지 가는 path의 최소합을 찾는 문제

Example:
- Input : [[2],[3,4],[6,5,7],[4,1,8,3]]
- Output : 11
- 2+3+5+1 = 11

Note:
top to bottom이지만 bottom에서 top으로 올라가는 방식으로 문제를 해결하는 것이 간단
이동할 수 있는 아래의 두 칸 중에서 작은 값을 선택하여 더하는 방식으로 해결

"""

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(len(triangle) - 2, -1, -1) :
            for j in range(len(triangle[i])) :
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
        return triangle[0][0]