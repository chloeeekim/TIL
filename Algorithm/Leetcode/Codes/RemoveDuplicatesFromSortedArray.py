"""

26. Remove Duplicates from Sorted Array : https://leetcode.com/problems/remove-duplicates-from-sorted-array/

정수로 이루어진 정렬된 리스트가 주어졌을 때,
주어진 리스트에서 겹치는 숫자들을 제외한 리스트를 만드는 문제
- in-place : 다른 리스트를 할당하지 말고 주어진 리스트 내에서 해결할 것
- 각 원소는 단 한 번씩만 나타나야 한다
- 새롭게 만들어진 리스트의 길이를 리턴
- 리턴한 길이의 뒷부분에는 리스트에 어떤 값이 있건 상관하지 않음

Example:
- Input : nums = [1,1,2]
- Output : length = 2, nums = [1,2, ...]

- Input : nums = [0,0,1,1,1,2,2,3,3,4]
- Output : length = 5, nums = [0,1,2,3,4, ...]

Note:
- Solution 1
리스트가 정렬되어 있기 때문에 다음에 나타나는 원소가 이전과 동일하다면 삭제하는 방법으로 구현
리스트 내에서 순서를 바꾸는 방법도 가능
- Solution 2
원소의 중복을 허용하지 않는 set을 이용
in-place 방법이 아니라고 생각했으나 Memory 사용량은 동일

"""

# Solution 1
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:        
        if not nums :
            return 0
        length = len(nums)
        now = nums[0]
        i = 1
        while (i < length) :
            if now == nums[i] :
                del nums[i]
                length -= 1
            else :
                now = nums[i]
                i += 1
        return i    

# Solution 2
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = list(set(nums))
        nums.sort()
        return len(nums)