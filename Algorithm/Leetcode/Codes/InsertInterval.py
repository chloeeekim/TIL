"""

57. Insert Interval : https://leetcode.com/problems/insert-interval/

겹치지 않는 범위의 리스트 intervals와 새로운 범위 하나가 주어졌을 때, 서로 겹치지 않도록 intervals를 업데이트 하는 문제
- 모든 범위들은 오름차순으로 정렬

Example:
- Input : intervals = [[1,3],[6,9]], newInterval = [2,5]
- Output : [[1,5],[6,9]]

- Input : intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
- Output : [[1,2],[3,10],[12,16]]

- Input : intervals = [], newInterval = [5,7]
- Output : [[5,7]]

- Input : intervals = [[1,5]], newInterval = [2,3]
- Output : [[1,5]]

- Input : intervals = [[1,5]], newInterval = [2,7]
- Output : [[1,7]]

Note:
intervals 리스트에 새 범위를 추가한 다음 첫 번째 인자를 기준으로 오름차순 정렬
결과 리스트가 비어있거나 다음 범위와 겹치지 않는 경우에는 다음 범위를 append
그렇지 않은 경우 두 번째 인자를 업데이트

"""

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x:x[0])
        res = []
        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        return res