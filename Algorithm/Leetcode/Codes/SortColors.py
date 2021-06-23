"""

75. Sort Colors : https://leetcode.com/problems/sort-colors/

길이 n의 리스트 nums가 주어졌을 때, 이를 정렬하는 문제
- nums 리스트는 0, 1, 2 세 가지 숫자로만 이루어진다
- in-place로 해결할 것

Example:
- Input : nums = [2,0,2,1,1,0]
- Output : [0,0,1,1,2,2]

- Input : nums = [2,0,1]
- Output : [0,1,2]

- Input : nums = [0]
- Output : [0]

- Input : nums = [1]
- Output : [1]

Note:
- Solution 1
Bubble sort로 해결
속도가 느린 편이지만 간단하게 구현 가능
- Solution 2
숫자가 3가지만 존재한다는 걸 이용
0은 리스트의 앞쪽으로, 2는 리스트의 뒤쪽으로 이동시키는 방식
bubble sort에 비해 속도가 굉장히 빠르다는 장점

"""

# Solution 1

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        for i in range(l):
            for j in range(l-i-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]

# Solution 2

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low, high, cur = 0, len(nums)-1, 0
        while cur <= high:
            if nums[cur] == 0:
                nums[low], nums[cur] = nums[cur], nums[low]
                low += 1
                cur += 1
            elif nums[cur] == 1:
                cur += 1
            else:
                nums[high], nums[cur] = nums[cur], nums[high]
                high -= 1