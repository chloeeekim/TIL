"""

1480. Running Sum of 1d Array : https://leetcode.com/problems/running-sum-of-1d-array/

리스트 nums가 주어졌을 때, running sum을 구하는 문제
- running sum이란 i번째 인자가 nums[0]부터 nums[i]까지의 합으로 이루어진 리스트를 의미한다

Example:
- Input : nums = [1,2,3,4]
- Output : [1,3,6,10]

- Input : [1,1,1,1,1]
- Output : [1,2,3,4,5]

- Input : [3,1,2,10,1]
- Output : [3,4,6,16,17]

Note:
in-place로 해결 가능

"""

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] = nums[i-1] + nums[i]
        return nums