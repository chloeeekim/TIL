"""

279. Perfect Squares : https://leetcode.com/problems/perfect-squares/

주어진 숫자가 최소 몇 개의 perfect square의 합으로 이루어져 있는지 확인하는 문제
- perfect square란 제곱수를 의미한다 (1, 4, 9, 16 등)

Example:
- Input : n = 12
- Output : 3
- 12 = 4 + 4 + 4

- Input : n = 13
- Output : 2
- 13 = 4 + 9

Note:
dp로 해결
가장 많은 경우의 수는 1의 합으로만 이루어지는 경우 (n)
recursive하게 해결하는 방법으로는 time limit에 걸림

"""

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] + [n for n in range(1, n+1)]
        for i in range(1, n+1):
            for j in range(1, int(sqrt(i))+1):
                dp[i] = min(dp[i], 1+dp[i-(j*j)])
        return dp[n]