"""

554. Brick Wall : https://leetcode.com/problems/brick-wall/

각 라인별 벽돌의 width가 포함된 리스트가 주어졌을 때, 벽돌을 최소한으로 가르는 vertical 라인을 찾는 문제
- 벽의 양쪽 끝에 선을 긋는 것은 포함되지 않는다 (무조건 0개의 벽돌을 가르게 되므로)

Example:
- Input : [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
- Output : 2
- 왼쪽에서부터 4번째에 라인을 그으면 된다

- Input : [[1],[1],[1]]
- Output : 3
- 양쪽 끝에는 선을 그을 수 없으므로, 무조건 벽돌 세 개를 지나는 경우만 존재한다

Note:
dict를 이용하여 해결
해당 벽돌이 끝나는 부분의 전체 width를 구했을 때,
width가 가장 많이 등장하는 경우가 최소한으로 벽돌을 가를 수 있는 vertical line이 된다

"""

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        counts = {}
        for i in range(len(wall)):
            width = 0
            for j in range(len(wall[i])-1):
                width += wall[i][j]
                counts[width] = 1 if width not in counts else counts[width]+1
        return len(wall)-max(counts.values()) if counts else len(wall)