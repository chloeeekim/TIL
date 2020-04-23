"""

560. Subarray Sum Equals K : https://leetcode.com/problems/subarray-sum-equals-k/

정수로 이루어진 리스트와 k가 주어졌을 때, 합이 k가 되는 continuous subarray의 총 개수를 구하는 문제
- 리스트의 길이는 1 이상 20,000 이하이다
- 리스트에 포함된 원소는 [-1000,1000] 범위이며, k의 범위는 [-1e7,1e7]이다

Example:
- Input : nums = [1,1,1], k = 2
- Output : 2

Note:
brute force로 푸는 경우 time limit
continuous subarray이므로 dict를 사용하여 이전에 발견된 부분합을 저장해놓는 방식으로 해결

"""

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res, temp, seen = 0, 0, {0: 1}
        for num in nums:
            temp += num
            if temp-k in seen:
                res += seen[temp-k]
            seen[temp] = 1 if temp not in seen else seen[temp]+1
        return res