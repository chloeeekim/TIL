"""

1232. Check If It Is a Straight Line : https://leetcode.com/problems/check-if-it-is-a-straight-line/

포인트들의 리스트 coordinates가 주어졌을 때, 모든 점들이 하나의 직선상에 존재하는지 확인하는 문제
- coordinates 리스트의 길이는 2 이상 1000 이하이다
- coordinates는 [x,y]의 쌍으로 이루어진다
- 주어진 리스트에 중복되는 포인트는 없다

Example:
- Input : coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
- Output : true

- Input : coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
- Output : false

Note:
처음에는 기울기를 구하는 방식으로 시도했으나, y축에 수평한 직선 상의 점이 주어지는 경우 0으로 나눠야 하므로 구할 수 없다
따라서 기울기를 직접 구하지 않고, x값의 차이와 y값의 차이를 통해 기울기가 동일한지 확인

"""

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        xdiff = coordinates[0][0]-coordinates[1][0]
        ydiff = coordinates[0][1]-coordinates[1][1]
        for i in range(2, len(coordinates)):
            xtemp = coordinates[i-1][0]-coordinates[i][0]
            ytemp = coordinates[i-1][1]-coordinates[i][1]
            if xtemp*ydiff != ytemp*xdiff:
                return False
        return True