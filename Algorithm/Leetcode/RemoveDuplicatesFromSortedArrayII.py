"""

80. Remove Duplicates from Sorted Array II : https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

정수로 이루어진 정렬된 리스트가 주어졌을 때,
하나의 숫자는 최대 2번만 등장하도록 겹치는 숫자들을 제외한 리스트를 만드는 문제
- in-place : 다른 리스트를 할당하지 말고 주어진 리스트 내에서 해결할 것
- 각 원소는 최대 두 번씩만 나타나야 한다
- 새롭게 만들어진 리스트의 길이를 리턴
- 리턴한 길이의 뒷부분에는 리스트에 어떤 값이 있건 상관하지 않음

Example:
- Input : nums = [1,1,1,2,2,3]
- Output : length = 5, nums = [1,1,2,2,3, ...]

- Input : nums = [0,0,1,1,1,1,2,3,3]
- Output : length = 7, nums = [0,0,1,1,2,3,3, ...]

Note:
나타나는 원소가 이전과 동일한 경우 count를 하여 2번을 초과하여 나타나는 경우에 삭제하는 방법으로 구현
리스트 내에서 순서를 바꾸는 방법도 가능

"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums :
            return 0
        now = nums[0]
        count, i = 1, 1
        while i < len(nums) :
            if nums[i] == now :
                if count < 2 :
                    count += 1
                    i += 1
                else :
                    del nums[i]
            else :
                now = nums[i]
                count = 1
                i += 1
        return len(nums)