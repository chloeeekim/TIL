"""

436. Find Right Interval : https://leetcode.com/problems/find-right-interval/

intervals가 주어졌을 때, right interval의 인덱스를 구하는 문제
- interval i의 right interval이란 start_j >= end_i이며 start_j가 최소가 되는 interval을 의미한다
- right interval이 존재하지 않는 경우 -1

Example:
- Input : intervals = [[1,2]]
- Output : -1

- Input : intervals = [[3,4],[2,3],[1,2]]
- Output : [-1,0,1]
- [3,4]의 right interval은 없으므로 -1
[2,3]의 right interval은 [3,4]이므로 인덱스 0
[1,2]의 right interval은 [2,3]이므로 인덱스 1

= Input : intervals = [[1,4],[2,3],[3,4]]
- Output : [-1,2,-1]

Note:
start 값과 index 값을 튜플로 하여 정렬
bisect_left를 사용하여 효율적으로 서치할 수 있도록 함

"""

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        if len(intervals) < 2:
            return [-1]
        starts = [(start, idx) for (idx, (start, _)) in enumerate(intervals)]
        starts.sort()
        res = []
        for _, end in intervals:
            i = bisect_left(starts, (end, 0))
            if i == len(intervals):
                res.append(-1)
            else:
                res.append(starts[i][1])
        return res