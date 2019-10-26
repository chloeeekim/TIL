"""

162. Find Peak Element : https://leetcode.com/problems/find-peak-element/

숫자들로 이루어진 리스트 nums가 주어졌을 때, peak element를 찾는 문제
- nums[i]와 nums[i+1]은 같지 않다
- peak element란 주변 원소보다 큰 원소를 의미한다
- 여러 개의 peak element가 존재할 수 있으며, 그 중 무엇이든 하나를 찾으면 된다
- nums[-1]과 nums[n]은 -∞로 가정한다

Example:
- Input : [1,2,3,1]
- Output : 2
- peak element : 3

- Input : [1,2,1,3,5,6,4]
- Output : 1 or 5
- peak element : 2 (index 1) or 6 (index 5)

Note:
- Solution 1
nums[-1]은 무조건 nums[0]보다 작고, 아무 peak element만 찾으면 되므로,
앞에서부터 다음 원소가 작아지는 원소를 찾으면 된다
만약 리스트를 다 돌았는데도 없다면 마지막 원소가 peak element가 된다
- Solution 2
최댓값은 무조건 peak element이므로 최댓값의 인덱스를 구하면 된다

"""

# Solution 1
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        for i in range(len(nums)-1) :
            if nums[i+1] < nums[i] :
                return i
        return len(nums) - 1

# Solution 2
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        return nums.index(max(nums))