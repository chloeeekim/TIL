"""

724. Find Pivot Index : https://leetcode.com/problems/find-pivot-index/

숫자들로 이루어진 리스트 nums가 주어졌을 때, pivot이 되는 인덱스를 찾는 문제
- pivot을 기준으로 두 sub list의 합이 동일한 경우가 pivot index
- pivot index가 없는 경우, -1을 리턴
- pivot index가 여러 개가 존재하는 경우, 가장 왼쪽에 있는 값을 리턴

Example:
- Input : [1,7,3,6,5,6]
- Output : 3
- nums[3]을 기준으로 1+7+3 = 5+6

- Input : [1,2,3]
- Output : -1
- pivot index가 존재하지 않는 경우

Note:
pivot index를 0에서부터 시작하여 왼쪽과 오른쪽 sub list의 합을 비교

"""

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left, right = 0, sum(nums)
        for i in range(len(nums)) :
            right -= nums[i]
            if left == right :
                return i
            left += nums[i]
        return -1