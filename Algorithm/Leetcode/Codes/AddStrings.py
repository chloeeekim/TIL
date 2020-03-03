"""

415. Add Strings : https://leetcode.com/problems/add-strings/

음수가 아닌 두 개의 정수가 문자열로 주어졌을 때, 두 값을 더하는 문제
- num1과 num2의 길이는 5100 미만이다
- num1과 num2는 0-9까지의 숫자만을 포함하며, 의미 없는 0으로 시작하지 않는다
- built-in BigInteger library를 사용하거나 input을 integer로 직접적으로 변환하지 말 것

Example:
- Input : num1 = "123456789", num2 = "987654321"
- Output : "1111111110"

Note:
문자열의 뒤에서부터 더해 res 문자열에 추가하는 방법
문자열 두 개의 길이가 다른 경우 남은 문자열만 따로 확인

"""

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res, up, len1, len2 = "", 0, len(num1) - 1, len(num2) - 1
        while len1 >= 0 and len2 >= 0 :
            calc = int(num1[len1]) + int(num2[len2]) + up
            up = 1 if calc > 9 else 0
            calc = calc - 10 if calc > 9 else calc
            res = str(calc) + res
            len1 -= 1
            len2 -= 1
        remain = num1 if len1 >= 0 else num2
        idx = len1 if len1 >= 0 else len2
        while idx >= 0 :
            calc = int(remain[idx]) + up
            up = 1 if calc > 9 else 0
            calc = calc - 10 if calc > 9 else calc
            res = str(calc) + res
            idx -= 1
        if up == 1 :
            return "1" + res
        else :
            return res