"""

326. Power of Three : https://leetcode.com/problems/power-of-three/

숫자가 하나 주어졌을 때, 해당 숫자가 3의 제곱수인지를 구하는 문제

Example:
- Input : 27
- Output : true

- Input : 0
- Output : false

- Input : 9
- Output : true

- Input : 45
- Output : false

Note:
3의 제곱수를 구해가면서 n과 비교
n과 동일한 제곱수가 있는 경우 true, n보다 커지게 되면 false

"""

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        power = 1
        while power <= n :
            if power == n :
                return True
            power *= 3
        return False