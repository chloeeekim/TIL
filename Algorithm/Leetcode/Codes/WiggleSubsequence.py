"""

376. Wiggle Subsequence : https://leetcode.com/problems/wiggle-subsequence/

정수로 이루어진 리스트 nums가 주어졌을 때, 가장 긴 wiggle subsequence의 길이를 구하는 문제
- subsequence란 원 순서를 변경하지 않고 원소를 제거하는 등으로 만들어지는 sequence를 의미한다
- wiggle sequence란 다음 원소와의 차이가 +, -로 번갈아나오는 경우를 의미한다
- nums 리스트는 0 이상 1000 이하의 숫자로 이루어진다

Example:
- Input : nums = [1,7,4,9,2,5]
- Output : 6
- 전체 sequence가 wiggle -> (6, -3, 5, -7, 3)

- Input : nums = [1,17,5,10,13,15,10,5,16,8]
- Output : 7
- [1, 17, 10, 13, 10, 16, 8]가 wiggle -> (16, -7, 3, -3, 6, -8)

- Input : nums = [1,2,3,4,5,6,7,8,9]
- Output : 2

Note:
숫자가 커지는 경우 up, 작아지는 경우를 down으로 두고
wiggle이어야 하므로 down은 up에서, up은 down에서 더하는 방식

"""

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        down, up = 1, 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                up = down+1
            elif nums[i] < nums[i-1]:
                down = up+1
        return max(up, down)