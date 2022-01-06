"""

1094. Car Pooling : https://leetcode.com/problems/car-pooling/

capacity만큼의 빈 좌석이 있는 차량과 trips가 주어졌을 때, 모든 승객을 옮길 수 있는지 확인하는 문제
- trip[i] = [numPassengers, from, to]의 형태로 주어진다
- trips의 길이는 1 이상 1000 이하이다
- numPassengers는 1 이상 100 이하이다
- from, to는 0 이상 1000 이하이다

Example:
- Input : trips = [[2,1,5],[3,3,7]], capacity = 4
- Output : false

- Input : trips = [[2,1,5],[3,3,7]], capacity = 5
- Output : true

Note:
from, to가 1000 이하이므로 고정 길이의 리스트를 생성하여 처리
승객을 태우는 경우 +, 승객이 내리는 경우 -를 하여 현재 승객의 수를 확인

"""

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        temp = [0] * 1001
        for p, tfrom, tto in trips:
            temp[tfrom] += p
            temp[tto] -= p
        current = 0
        for t in temp:
            current += t
            if current > capacity:
                return False
        return True