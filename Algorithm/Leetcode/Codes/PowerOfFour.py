"""

342. Power of Four : https://leetcode.com/problems/power-of-four/

숫자가 하나 주어졌을 때, 해당 숫자가 4의 제곱수인지를 구하는 문제

Example:
- Input : 16
- Output : true

- Input : 5
- Output : false

Note:
4의 제곱수를 구해가면서 n과 비교
n과 동일한 제곱수가 있는 경우 true, n보다 커지게 되면 false

"""

class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        power = 1
        while power <= num :
            if power == num :
                return True
            power *= 4
        return False