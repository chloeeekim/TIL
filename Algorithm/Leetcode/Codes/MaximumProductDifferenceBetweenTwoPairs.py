"""

1913. Maximum Product Difference Between Two Pairs : https://leetcode.com/problems/maximum-product-difference-between-two-pairs/

숫자로 이루어진 리스트에서 maximum product difference를 구하는 문제
- product difference란 (a,b)와 (c,d)의 두 pair가 있을 때, (a*b)-(c*d)로 정의된다
- 주어지는 리스트의 길이는 4 이상 10,000 이하이다
- 주어지는 숫자는 모두 1 이상의 양수이다

Example:
- Input : nums = [5,6,2,7,4]
- Output : 34
- (6,7)과 (2,4)를 선택

- Input : nums = [4,2,5,9,7,4,8]
- Output : 64
- (9,8)과 (2,4)를 선택

Note:
리스트 내에 음수가 존재하지 않으므로, maximum product difference는 가장 큰 값들의 곱 - 가장 작은 값들의 곱이 된다
nums 리스트를 정렬하여 가장 큰 값 두 개와 가장 작은 값 두 개로 product difference를 계산

"""

class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums = sorted(nums)
        return nums[-1]*nums[-2] - nums[0]*nums[1]