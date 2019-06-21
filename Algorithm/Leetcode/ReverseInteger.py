"""

7. Reverse Integer : https://leetcode.com/problems/reverse-integer/

주어진 32-bit 정수를 뒤집는 문제
- 32-bit signed integer 기준 (범위 : -2^31 ~ 2^31 - 1)
- 해당 범위를 넘는 경우, 0을 출력

Example:
- Input : x = 123
- Output : 321

- Input : x = -123
- Output : -321

- Input : 120
- Output : 21

Note:
reverse 문자열 구하는 법 : [::-1]
제곱은 **와 pow 둘 다 사용 가능

"""

class Solution:
    def reverse(self, x: int) -> int:
        if x > 0 :
            res = int(str(x)[::-1])
        else :
            res = -1 * int(str(x * -1)[::-1])
        
        if -2**31 <= res <= 2**31 - 1 :
            return res
        else :
            return 0