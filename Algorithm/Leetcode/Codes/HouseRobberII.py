"""

213. House Robber II : https://leetcode.com/problems/house-robber-ii/

각 집에서 얻을 수 있는 이익이 리스트로 주어졌을 때, 최대로 얻을 수 있는 이익을 구하는 문제
- 두 개의 인접한 집을 방문할 수 없다
- 집들은 원형으로 연결되어 있다 (즉, 첫 번째 집과 마지막 집은 인접해 있다)

Example:
- Input : [2,3,2]
- Output : 3
- 첫 번째 집과 세 번째 집은 인접해 있으므로 함께 방문할 수 없다

- Input : [1,2,3,1]
- Output : 4
- 1 + 3 = 4

Note:
DP로 해결
해당 집까지 얻을 수 있는 최대 이익을 리스트에 저장하는 방식
첫 번째 집과 마지막 집을 함께 방문할 수 없으므로,
첫 번째 집을 제외하는 경우와 마지막 집을 제외하는 경우 두 가지로 나눠서 해결

"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) < 2 :
            return max(nums)
        arr1 = [0, 0] + nums[:-1]
        for i in range(2, len(arr1)) :
            arr1[i] = max(arr1[i-2] + arr1[i], arr1[i-1])
        arr2 = [0, 0] + nums[1:]
        for i in range(2, len(arr2)) :
            arr2[i] = max(arr2[i-2] + arr2[i], arr2[i-1])
        return max(arr1 + arr2)