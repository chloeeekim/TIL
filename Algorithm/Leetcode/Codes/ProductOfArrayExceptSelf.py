"""

238. Product of Array Except Self : https://leetcode.com/problems/product-of-array-except-self/

숫자가 포함된 nums 리스트가 주어졌을 때, 해당 인덱스의 값을 제외한 나머지의 곱으로 이루어진 output 리스트를 구하는 문제
- division을 사용하지 말 것

Example:
- Input : [1,2,3,4]
- Output : [24,12,8,6]

Note:
왼쪽과 오른쪽 각각에서부터 곱을 구해 리스트에 저장
특정 인덱스를 기준으로 leftarr의 값은 왼쪽에 위치한 subarray의 곱이 되고,
rightarr의 값은 오른쪽에 위치한 subarray의 곱이 된다

"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftarr, rightarr, left, right = [1 for _ in nums], [1 for _ in nums], 1, 1
        for i in range(len(nums)):
            leftarr[i] = left
            rightarr[-1-i] = right
            left *= nums[i]
            right *= nums[-1-i]
        return [leftarr[i]*rightarr[i] for i in range(len(nums))]