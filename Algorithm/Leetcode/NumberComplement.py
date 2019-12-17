"""

476. Number Complement : https://leetcode.com/problems/number-complement/

양의 정수 하나가 주어졌을 때, 이를 2진수로 나타낸 숫자의 보수를 찾는 문제
- 주어지는 숫자는 32-bit signed integer의 범위이다
- 주어지는 숫자를 2진수로 변환한 경우 leading zero는 없다고 가정한다

Example:
- Input : 5
- Output : 2
- 5 = 101(2)이므로 5의 보수는 010(2) = 2

- Input : 1
- Output : 0
- 1 = 1(2)이므로 1의 보수는 0(2) = 0

Note:
~ 연산을 사용하면 음수로 변환되므로,
주어지는 숫자에 해당하는 길이만큼 1로 이루어진 이진수를 생성하여 xor 연산(^)을 하는 방법

"""

class Solution:
    def findComplement(self, num: int) -> int:
        ones = 1
        for i in range(len(bin(num)) - 3) :
            ones = ones * 2 + 1
        return num ^ ones