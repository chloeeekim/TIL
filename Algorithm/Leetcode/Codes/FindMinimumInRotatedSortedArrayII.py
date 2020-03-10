"""

154. Find Minimum in Rotated Sorted Array II : https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/

증가수열로 정렬된 리스트가 rotated된 상태로 주어졌을 때, 가장 작은 값을 찾는 문제
- 중복되는 값이 존재할 수 있다

Example:
- Input : [1,3,5]
- Output : 1

- Input : [2,2,2,0,1]
- Output : 0

Note:
Find Minimum in Rotated Sorted Array 문제와 동일한 방법
수열이 더 이상 증가하지 않으면 해당 값이 최소값
리스트 전체가 증가하기만 하는 경우 리스트의 첫 번째 값이 최소값
의문) 리스트 내의 중복 여부가 문제 난이도에 영향을 미치나?

"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        for i in range(len(nums) - 1) :
            if nums[i] > nums[i+1] :
                return nums[i+1]
        return nums[0]