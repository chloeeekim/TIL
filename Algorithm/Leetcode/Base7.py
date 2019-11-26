"""

504. Base 7 : https://leetcode.com/problems/base-7/

숫자가 주어졌을 때, 7진수로 변환하는 문제
- 결과는 문자열의 형태로 나타내어야 한다

Example:
- Input : 100
- Output : "202"

- Input : -7
- Output : "-10"

Note:
7보다 작은 경우 값을 문자열로 변환하여 그대로 리턴
7을 나눈 나머지가 해당 자릿수의 값

"""

class Solution:
    def convertToBase7(self, num: int) -> str:
        if abs(num) < 7 :
            return str(num)
        res, negative = "", False if num >= 0 else True
        num = abs(num)
        while num >= 7 :
            num, mod = divmod(num, 7)
            res = str(mod) + res
        res = str(num) + res
        return res if not negative else '-' + res