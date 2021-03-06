"""

283. Move Zeroes : https://leetcode.com/problems/move-zeroes/

0이 포함된 리스트 nums가 주어졌을 때, 모든 0을 리스트의 뒷부분으로 이동시키는 문제
- 0이 아닌 숫자들이 나타나는 순서는 유지되어야 한다
- in-place로 해결할 것

Example:
- Input : [0,1,0,3,12]
- Output : [1,3,12,0,0]

Note:
- Solution 1
리스트를 확인하면서 0이 나타나면 해당 원소를 지우고 뒤에 0을 append하는 방식
리스트의 뒷부분에 0이 붙게 되므로, 몇 개의 0이 나타났는지를 확인하여 반복문 종료
- Solution 2
리스트에 추가/삭제하는 방식은 효율적이지 않으므로,
0이 아닌 숫자를 앞으로 옮긴 이후 남은 리스트를 전부 0으로 만들어버리는 방식

"""

# Solution 1

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        zero_count, i = 0, 0
        while length - i != zero_count :
            if nums[i] == 0 :
                del nums[i]
                nums.append(0)
                zero_count += 1
            else :
                i += 1

# Solution 2

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nidx = 0
        for num in nums:
            if num:
                nums[nidx] = num
                nidx += 1
        for i in range(nidx, len(nums)):
            nums[i] = 0