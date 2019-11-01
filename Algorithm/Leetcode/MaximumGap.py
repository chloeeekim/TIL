"""

164. Maximum Gap : https://leetcode.com/problems/maximum-gap/

정렬되지 않은 리스트가 주어졌을 때,
해당 리스트가 정렬된 상태일 때 각 원소들 사이의 차의 최대값을 구하는 문제
- 리스트의 원소가 2개 미만일 경우 0을 리턴한다

Example:
- Input : [3,6,9,1]
- Output : 3
- 정렬하면 [1,3,6,9]가 되고, 차가 최대값이 되는 경우는 (3,6)과 (6,9) 두 가지

- Input : [10]
- Output : 0
- 리스트의 원소가 2개 미만이므로 0을 리턴

Note:
입력으로 들어오는 리스트를 정렬 후 차의 최대값을 구하는 방식

"""

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2 :
            return 0
        nums.sort()
        res = nums[1] - nums[0]
        for i in range(1, len(nums) - 1) :
            res = max(nums[i+1] - nums[i], res)
        return res