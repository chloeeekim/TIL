"""

674. Longest Continuous Increasing Subsequence : https://leetcode.com/problems/longest-continuous-increasing-subsequence/

정렬되지 않은 숫자가 포함된 list가 주어졌을 때, longest continuous increasing subsequence의 길이를 구하는 문제
- 주어지는 list의 길이는 10,000을 넘지 않는다

Example:
- Input : [1,3,5,4,7]
- Output : 3
- lis = [1,3,5]. [1,3,5,7]은 continuous하지 않으므로 제외

- Input : [2,2,2,2,2]
- Output : 1
- lis = [2]

Note:
continuous한 subsequence여야 하므로 바로 이전 값과 비교하여 길이를 nums에 저장
증가하지 않는 경우 길이를 1부터 다시 시작

"""

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        count = [1 for _ in nums]
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                count[i] = count[i-1]+1
        return max(count)