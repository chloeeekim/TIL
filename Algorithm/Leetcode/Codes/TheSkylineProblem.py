"""

218. The Skyline Problem : https://leetcode.com/problems/the-skyline-problem/

건물들의 높이가 주어졌을 때, 건물들로 인해 만들어지는 skyline을 구하는 문제
- 각 건물들의 정보는 [left, right, height]로 주어진다
- 모든 건물은 완벽한 직사각형이며, 높이 0인 지면에 맞닿아있다고 가정한다
- skyline은 x축으로 정렬된 key points들이며, 각 높이에 해당하는 왼쪽 시작점을 의미한다

Example:
- Input : buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
- Output : [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]

- Input : buildings = [[0,2,3],[2,5,3]]
- Output : [[0,3],[5,0]]]

Note:
건물의 시작점과 끝점을 나누어서 sorted list로 관리
두 번째 예시 같은 경우 때문에 같은 위치인 경우 높이가 높은 것을 우선시하기 위하여 -height로 정렬
건물이 없거나 끝나는 경우를 위하여 지면(높이 0)을 추가

"""

from sortedcontainers import SortedList

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        heights = []
        for start, end, height in buildings:
            heights.append([start, -height])
            heights.append([end, height])
        heights = sorted(heights)
        b, ans = SortedList([0]), []
        for x, h in heights:
            if h > 0:
                b.remove(h)
            else:
                b.add(-h)
            if not ans or ans[-1][1] != b[-1]:
                ans.append([x, b[-1]])            
        return ans