"""

908. Smallest Range I : https://leetcode.com/problems/smallest-range-i/

정수로 이루어진 리스트 nums와 정수 k가 주어졌을 때, 가능한 가장 작은 범위를 찾는 문제
- 각 원소 nums[i]는 [nums[i]-k, nums[i]+k] 범위 내의 값을 가질 수 있다
- 위 operation을 한 번 시행한 후, nums 리스트 내의 가장 큰 값과 가장 작은 값의 차이를 구한다

Example:
- Input : nums = [1], k = 0
- Output : 0

- Input: nums = [0,10], k = 2
- Output: 6
- [2, 8]로 변경할 수 있다

- Input: nums = [1,3,6], k = 3
- Output: 0
- [4, 4, 4]로 변경할 수 있다

Note:
해당 리스트의 최대/최소값에 k를 더하거나 빼는 경우만 고려
0보다 작은 음수값이 나오는 경우 범위가 넓어지는 것이므로 0을 취한다

"""

class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        diffnums = max(nums) - min(nums)
        return diffnums - 2 * k if diffnums - 2 * k > 0 else 0