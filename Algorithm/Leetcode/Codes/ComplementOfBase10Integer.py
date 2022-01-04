"""

1009. Complement of Base 10 Integer : https://leetcode.com/problems/complement-of-base-10-integer/

주어진 정수의 compliment를 구하는 문제
- 이진수로 변환했을 때 0과 1을 서로 바꾸어 준 경우를 compliment로 정의한다

Example:
- Input : n = 5
- Output : 2
- 5 = "101"이므로 "010" = 2

- Input : n = 7
- Output : 0
- 7 = "111"이므로 "000" = 0

- Input : n = 10
- Output : 5
- 10 = "1010"이므로 "0101" = 5

Note:
format 함수를 사용하여 binary string으로 변환하고, int 함수를 사용해 10진수로 변환
python에서 2진수로 변환하는 방법은 bin() 함수를 사용하는 것 이외에 format() 함수를 사용할 수도 있다
format(n, "b") 형식으로 사용하면 접두어 제외 가능 ("#b"로 인자를 넘기면 접두어가 붙음)

"""

class Solution:
    def bitwiseComplement(self, n: int) -> int:
        b = format(n, "b")
        c = ""
        for i in b:
            c += "0" if i == "1" else "1"
        return int(c, 2)