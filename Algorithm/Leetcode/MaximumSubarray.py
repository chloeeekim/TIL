"""

53. Maximum Subarray : https://leetcode.com/problems/maximum-subarray/

정수로 이루어진 수열에서 합이 최대가 되는 연속 부분 수열을 찾는 문제

Example:
- Input : [-2,1,-3,4,-1,2,1,-5,4]
- Output : 6
- [4,-1,2,1]

Note:
res는 전체 subarray의 합 중에서 가장 큰 값
temp는 현재의 subarray의 합
nums[i]를 더했는데 nums[i]보다 작은 경우 최대합의 부분수열이 될 수 없음

"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res, temp = nums[0], nums[0]
        for i in range(1, len(nums)) :
            temp += nums[i]
            if temp < nums[i] :
                temp = nums[i]
            res = max(res, temp)
        return res