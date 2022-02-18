"""

435. Non-overlapping Intervals : https://leetcode.com/problems/non-overlapping-intervals/

intervals가 주어졌을 때, 남은 interval들이 non-overlapping이 되도록 지워야 하는 최소 개수의 interval을 구하는 문제
- interval은 [start, end]의 형식으로 주어진다

Example:
- Input : intervals = [[1,2],[2,3],[3,4],[1,3]]
- Output : 1
- [1,3]만 지우면 된다

- Input : intervals = [[1,2],[1,2],[1,2]]
- Output : 2
- 두 개의 [1,2]를 지워야 한다

= Input : intervals = [[1,2],[2,3]]
- Output : 0

Note:
정렬하여 greedy하게 해결
겹치는 경우 end 값이 큰 interval을 우선으로 삭제

"""

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        count, last = 0, intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] < last[1]:
                count += 1
                if intervals[i][1] < last[1]:
                    last = intervals[i]
            else:
                last = intervals[i]
        return count