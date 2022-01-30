"""

1005. Maximize Sum of Array After K Negations : https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/

정수로 이루어진 리스트 nums가 주어졌을 때, 아래와 같이 k번 변경한 후의 최대합을 구하는 문제
- nums[i]를 -nums[i]로 변경한다
- i는 동일한 인덱스로 여러 번 선택될 수 있다

Example:
- Input : nums = [4,2,3], k = 1
- Output : 5
- [4,-2,3]

- Input : nums = [3,-1,0,2], k = 3
- Output : 6
- index를 (1,2,2)로 선택하여 [3,1,0,2]를 만든다

- Input : nums = [2,-3,-1,5,-4], k = 2
- Output : 13
- [2,3,-1,5,4]

Note:
매번 최소값에 -1을 곱하는 것이 최대합을 만드는 방법
시간 효율을 위해 SortedList를 사용

"""

from sortedcontainers import SortedList

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        snums = SortedList(nums, key=lambda x: -x)
        for i in range(k):
            p = snums.pop()
            snums.add(-p)
        return sum(snums)