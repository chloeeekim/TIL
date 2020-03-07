"""

12. Integer to Roman : https://leetcode.com/problems/integer-to-roman/

정수가 주어졌을 때, 로마 숫자로 변환하는 문제
- 각 문자(symbol)별 해당하는 값은 아래와 같다
  -- I : 1 / V : 5 / X : 10 / L : 50 / C : 100 / D : 500 / M : 1000
- 왼쪽에서 오른쪽으로 읽으며, 큰 숫자에서 작은 숫자의 순서로 작성된다
- 작은 값에 해당하는 문자가 큰 값에 해당하는 문자의 왼쪽에 위치할 경우, 그 값만큼을 뺀다 (ex. 4 : IV)

Example:
- Input : 3
- Output : "III"

- Input : 4
- Output : "IV"

- Input : 9
- Output : "IX"

- Input : 58
- Output : "LVIII"
- L = 50 + V = 5 + III = 3

- Input : 1994
- Output : "MCMXCIV"
- M = 1000 + CM = 900 + XC = 90 + IV = 4

Note:
dict 사용 (key : 숫자 / value : 해당하는 로마 숫자(문자))
십 단위로 잘라서 해당 숫자의 범위에 따라 적절한 문자로 변환
참고) 더 깔끔하게 해결할 수 있는 방법?

"""

class Solution:
    def intToRoman(self, num: int) -> str:
        dict = {1 : 'I', 5 : 'V', 10 : 'X', 50 : 'L', 100 : 'C', 500 : 'D', 1000 : 'M'}
        res, count = "", 1
        while num > 0 :
            num, mod = divmod(num, 10)
            if mod > 0 and mod <= 3 :
                res = dict[1 * count] * mod + res
            elif mod == 4 :
                res = dict[1 * count] + dict[5 * count] + res
            elif mod == 5 :
                res = dict[5 * count] + res
            elif mod > 5 and mod <= 8 :
                res = dict[5 * count] + dict[1 * count] * (mod - 5) + res
            elif mod > 8 :
                res = dict[1 * count] + dict[10 * count] + res
            count *= 10
        return res