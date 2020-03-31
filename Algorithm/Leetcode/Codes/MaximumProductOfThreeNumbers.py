"""

628. Maximum Product of Three Numbers : https://leetcode.com/problems/maximum-product-of-three-numbers/

정수로 이루어진 array가 주어졌을 때, 3개의 숫자의 곱으로 만들 수 있는 가장 큰 수를 구하는 문제
- 주어지는 array의 길이는 [3, 10^4] 범위이며, 모든 element는 [-1000, 1000] 범위이다
- 어떠한 세 숫자의 곱도 32-bit signed integer의 범위를 넘지 않는다

Example:
- Input : [1,2,3]
- Output : 6

- Input : [1,2,3,4]
- Output : 24

Note:
array를 정렬하여 해결
가장 큰 세 수의 곱과 가장 작은 수 두 개와 가장 큰 수의 곱을 비교
음수일 경우를 고려하여 가장 작은 수 두 개를 선택

"""

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums = sorted(nums)
        res = max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])
        return res