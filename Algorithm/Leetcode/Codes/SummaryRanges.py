"""

228. Summary Ranges : https://leetcode.com/problems/summary-ranges/

정렬된 unique한 정수 리스트가 커버하는 범위를 찾는 문제
- 범위 [a, b]는 "a->b"로 표시하며, a는 b가 아니다
- 범위 [a, b]에서 a가 b와 동일한 경우, "a"로 표시한다
- 주어진 리스트는 오름차순으로 정렬되어 있다

Example:
- Input : nums = [0,1,2,4,5,7]
- Output : ["0->2","4->5","7"]

- Input : nums = [0,2,3,4,6,8,9]
- Output : ["0","2->4","6","8->9"]

- Input : nums = []
- Output : []

- Input : nums = [-1]
- Output : ["-1"]

- Input: nums = [0]
- Output: ["0"]

Note:
리스트에 값이 하나만 있는 경우 범위를 찾을 필요가 없으므로 해당 리스트의 값을 리턴
반복하면서 각 범위를 찾고 다음으로 넘어가는 방식

"""

import sys


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res, i, n = [], 0, len(nums)
        if n == 1:
            return [str(nums[0])]
        while i < n-1:
            start, end = nums[i], sys.maxsize
            while i < n-1 and nums[i]+1 == nums[i+1]:
                end = nums[i+1]
                i += 1
            if end == nums[i]:
                res.append(f"{start}->{end}")
            else:
                res.append(f"{start}")
            i += 1
            if i == n-1:
                res.append(str(nums[i]))
        return res
