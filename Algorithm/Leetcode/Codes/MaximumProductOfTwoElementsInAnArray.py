"""

1464. Maximum Product of Two Elements in an Array : https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/

숫자로 이루어진 리스트 nums에서 (nums[i]-1)*(nums[j]-1)의 최대값을 구하는 문제
- 주어지는 리스트의 길이는 2 이상 500 이하이다
- 주어지는 숫자는 모두 1 이상의 양수이다

Example:
- Input : nums = [3,4,5,2]
- Output : 12
- (4-1)*(5-1)=12

- Input : nums = [1,5,4,5]
- Output : 16

- Input : nums = [3,7]
- Output : 12

Note:
리스트 내에 음수가 존재하지 않으므로, 두 element의 곱이 가장 크려면 가장 큰 값들의 곱을 구하면 된다
nums 리스트를 정렬하여 해결

"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums = sorted(nums)
        return (nums[-1]-1)*(nums[-2]-1)