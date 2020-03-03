"""

172. Factorial Trailing Zeroes : https://leetcode.com/problems/factorial-trailing-zeroes/

정수 n이 주어졌을 때, n!의 뒤에 0이 몇 개가 나오는 지를 찾는 문제

Example:
- Input : 3
- Output : 0
- 3! = 6

- Input : 5
- Output : 1
- 5! = 120

Note:
10 = 2 X 5로만 나타나고, 2가 곱해지는 횟수가 5가 곱해지는 횟수보다 많으므로
5가 총 몇 번 곱해지는지를 확인하면 된다
5의 제곱수들은 5가 한 번씩 더 곱해지므로 그만큼 더 더해준다

"""

class Solution:
    def trailingZeroes(self, n: int) -> int:
        res = 0
        power = 5
        while power <= n :
            res += n // power
            power *= 5
        return res