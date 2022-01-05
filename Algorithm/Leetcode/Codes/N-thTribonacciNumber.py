"""

1137. N-th Tribonacci Number : https://leetcode.com/problems/n-th-tribonacci-number/

n번째 tribonacci number를 구하는 문제
- T0 = 0, T1 = 1, T2 = 1, Tn+3 = Tn + Tn+1 + Tn+2 이다
- n의 값은 0 이상 37 이하이다

Example:
- Input : n = 4
- Output : 4

- Input : n = 25
- Output : 1389537

Note:
dp 방식을 이용하여 해결
Tn의 값을 리스트에 저장하는 방식
아마 recursive하게 해결하면 time limit 걸릴 수도 있을 것 같음

"""

class Solution:
    def tribonacci(self, n: int) -> int:
        dp = defaultdict(int)
        dp[0], dp[1], dp[2] = 0, 1, 1
        for i in range(3, n+1):
            dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
        return dp[n]