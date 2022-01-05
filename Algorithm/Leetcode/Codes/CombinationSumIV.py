"""

377. Combination Sum IV : https://leetcode.com/problems/combination-sum-iv/

각각 다른 정수가 포함된 리스트 nums로 합이 target이 되도록 만들 수 있는 combination의 개수를 구하는 문제
- nums의 값은 모두 unique하다
- nums의 값은 1 이상 1000 이하의 정수이다
- target은 1 이상 1000 이하의 정수이다

Example:
- Input : nums = [1,2,3], target = 4
- Output : 7
- [1,1,1,1], [1,1,2], [1,2,1], [1,3], [2,1,1], [2,2], [3,1]

- Input : nums = [9], target = 3
- Output : 0

Note:
dp 방식으로 해결
각각의 값이 합이 되는 경우의 개수를 더하는 방식
index가 음수가 되는 경우 등에 대한 예외 처리를 하지 않기 위해 defaultdict 사용

"""

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1
        for i in range(target+1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i-num]
        return dp[target]