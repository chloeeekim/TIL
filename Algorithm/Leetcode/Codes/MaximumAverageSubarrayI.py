"""

643. Maximum Average Subarray I : https://leetcode.com/problems/maximum-average-subarray-i/

n개의 정수로 이루어진 list가 주어졌을 때, k의 길이를 가진 연속적인 subarray의 가장 큰 평균값을 구하는 문제
- 1 <= k <= n <= 30,000
- list 내의 원소는 -10,000 이상 10,000 이하이다

Example:
- Input : [1,12,-5,-6,50,3], k = 4
- Output : 12.75
- [12,-5,-6,50]의 평균값은 12.75

Note:
길이가 정해져 있으므로, 각 subarray의 합의 max 값을 구한 다음 길이로 나눠서 해결

"""

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxsum = sum(nums[:k])
        tmp = maxsum
        for i in range(1, len(nums)-k+1):            
            tmp += nums[i+k-1]
            tmp -= nums[i-1]
            maxsum = max(maxsum, tmp)
        return maxsum/k