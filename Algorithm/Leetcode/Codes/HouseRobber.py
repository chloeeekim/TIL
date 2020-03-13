"""

198. House Robber : https://leetcode.com/problems/house-robber/

각 집에서 얻을 수 있는 이익이 리스트로 주어졌을 때, 최대로 얻을 수 있는 이익을 구하는 문제
- 두 개의 인접한 집을 방문할 수 없다

Example:
- Input : [1,2,3,1]
- Output : 4
- 첫 번째 집(money = 1)과 세 번째 집(money = 3)

- Input : [2,7,9,3,1]
- Output : 12
- 2 + 9 + 1 = 12

Note:
DP로 해결
해당 집까지 얻을 수 있는 최대 이익을 리스트에 저장하는 방식

"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) < 2 :
            return max(nums)
        nums = [0, 0] + nums
        for i in range(2, len(nums)) :
            nums[i] = max(nums[i-2] + nums[i], nums[i-1])
        return max(nums)