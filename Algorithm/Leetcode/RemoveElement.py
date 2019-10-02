"""

27. Remove Element : https://leetcode.com/problems/remove-element/

정수로 이루어진 리스트와 정수가 하나 주어졌을 때,
주어진 리스트에서 주어진 정수를 제외한 리스트를 만드는 문제
- in-place : 다른 리스트를 할당하지 말고 주어진 리스트 내에서 해결할 것
- 주어진 정수를 제외한 리스트의 길이를 리턴
- 새로운 리스트의 원소 순서는 변경될 수 있음
- 리턴한 길이의 뒷부분에는 리스트에 어떤 값이 있건 상관하지 않음

Example:
- Input : nums = [3,2,2,3], val = 3
- Output : length = 2, nums = [2,2, ...]

- Input : nums = [0,1,2,2,3,0,4,2], val = 2
- Output : length = 5, nums = [0,1,3,0,4, ...]
- nums의 첫 5개의 원소에 0, 1, 3, 0, 4가 포함되어 있으면 정답 처리

Note:
val과 동일한 원소가 있으면 리스트에서 삭제하는 방법으로 구현
리스트 내에서 순서를 바꾸는 방법도 가능

"""

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        length = len(nums)
        while i < length :
            if nums[i] == val :
                nums.remove(nums[i])
                length -= 1
                continue
            i += 1
        return len(nums)