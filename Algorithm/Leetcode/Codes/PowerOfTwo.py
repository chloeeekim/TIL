"""

231. Power of Two : https://leetcode.com/problems/power-of-two/

숫자가 하나 주어졌을 때, 해당 숫자가 2의 제곱수인지를 구하는 문제

Example:
- Input : 1
- Output : true
- 2^0 = 1

- Input : 16
- Output : true
- 2^4 = 16

- Input : 218
- Output : false

Note:
2의 제곱수를 구해가면서 n과 비교
n과 동일한 제곱수가 있는 경우 true, n보다 커지게 되면 false

"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        power = 1
        while power <= n :
            if power == n :
                return True
            power *= 2
        return False