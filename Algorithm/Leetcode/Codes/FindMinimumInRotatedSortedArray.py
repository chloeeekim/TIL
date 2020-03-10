"""

153. Find Minimum in Rotated Sorted Array : https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

증가수열로 정렬된 리스트가 rotated된 상태로 주어졌을 때, 가장 작은 값을 찾는 문제
- 중복되는 값은 없다고 가정한다

Example:
- Input : [3,4,5,1,2]
- Output : 1

- Input : [4,5,6,7,0,1,2]
- Output : 0

Note:
수열이 더 이상 증가하지 않으면 해당 값이 최소값
리스트 전체가 증가하기만 하는 경우 리스트의 첫 번째 값이 최소값

"""

class Solution:
    def findMin(self, nums: List[int]) -> int :
        for i in range(len(nums) - 1) :
            if nums[i] > nums[i+1] :
                return nums[i+1]
        return nums[0]