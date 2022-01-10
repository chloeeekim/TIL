"""

152. Maximum Product Subarray : https://leetcode.com/problems/maximum-product-subarray/

정수로 이루어진 리스트 nums가 주어졌을 때, contiguous한 non-empty subarray로 만들 수 있는 maximum product를 구하는 문제
- subarray는 contiguous한 subsequence를 의미한다
- maximum product는 32-bit 정수임이 보장된다

Example:
- Input : =nums = [2,3,-2,4]
- Output : 6
- [2, 3]

- Input : nums = [-2,0,-1]
- Output : 0
- [-2, -1]은 subarray가 아니므로 제외

Note:
vals를 각각 현재 포인트부터 시작하는 subarray, 이전부터 시작된 subarray의 최대/최소로 계산
음수의 경우를 고려하여 cmin을 확인 (음수와 음수가 곱해져서 양수가 되는 경우가 있으므로)

"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cmax, cmin = 1, 1
        res = nums[0]        
        for n in nums:
            vals = (n, n * cmax, n * cmin)
            cmax, cmin = max(vals), min(vals)			
            res = max(res, cmax)            
        return res