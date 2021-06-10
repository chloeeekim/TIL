"""

191. Number of 1 Bits : https://leetcode.com/problems/number-of-1-bits/

binary string이 주어졌을 때, '1' bit의 개수를 세는 문제

Example:
- Input : n = 00000000000000000000000000001011
- Output : 3

- Input : n = 00000000000000000000000010000000
- Output : 0

- Input : n = 11111111111111111111111111111101
- Output : 31

Note:
- Solution 1
숫자를 binary string으로 변환한 후, '1'의 개수를 count 함수로 확인
- Solution 2
Reverse Bits 문제와 비슷한 방식
1-bit씩 이동하면서 1의 개수를 세는 방법
"""

# Solution 1
class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')

# Solution 2
class Solution:
    def hammingWeight(self, n: int) -> int:
        count, power = 0, 31
        while n:
            if (n & 1) << power != 0:
                count += 1
            power -= 1
            n >>= 1
        return count