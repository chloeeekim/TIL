"""

190. Reverse Bits : https://leetcode.com/problems/reverse-bits/

주어진 string을 bit 단위로 뒤집는 문제
- 입력으로 주어지는 string은 0과 1로 이루어져 있다
- 입력으로 주어지는 binary string의 길이는 32이다
(참고) binary string이 주어지는 것이 아니라 int 값으로 주어진다

Example:
- Input : n = 00000010100101000001111010011100
- Output : 964176192
- 주어진 n을 뒤집으면 00111001011110000010100101000000이 된다

- Input : n = 11111111111111111111111111111101
- Output : 3221225471

Note:
- Solution 1
binary 문자열로 변경하여 뒤집은 다음, 다시 int 타입으로 변경하는 방법
bit 연산으로 해결하는 것보다 효율이 떨어진다
- Solution 2
1-bit씩 이동하면서 bit 연산으로 뒤집는 방법
shift 연산자도 동일하게 >>= 처럼 shift 연산 이후 할당하는 방식으로 사용 가능

"""

# Solution 1

class Solution:
    def reverseBits(self, n: int) -> int:
        revbits = bin(n)[::-1][:-2]
        if len(revbits) < 32:
            revbits += "0"*(32-len(revbits))
        return int(revbits, 2)

# Solution 2

class Solution:
    def reverseBits(self, n: int) -> int:
        rev, power = 0, 31
        while n:
            rev += (n & 1) << power
            power -= 1
            n >>= 1
        return rev