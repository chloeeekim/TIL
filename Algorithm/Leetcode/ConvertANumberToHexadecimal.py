"""

405. Convert a Number to Hexadecimal : https://leetcode.com/problems/convert-a-number-to-hexadecimal/

숫자가 주어졌을 때, 16진수 문자열로 변환하는 문제
- 16진수에 포함되는 모든 알파벳(a-f)는 소문자로 나타내어야 한다
- 16진수 문자열은 0을 나타내는 것이 아닌 이상 문자열의 앞에 여분의 0이 포함되지 않아야 한다
- 주어지는 숫자는 32-bit signed integer 범위이다
- 숫자를 16진수로 변환하는 라이브러리나 함수 등을 사용하지 말 것

Example:
- Input : 26
- Output : "1a"

- Input : -1
- Output : "ffffffff"

Note:
숫자를 16으로 계속 나누어가며 각 자릿수를 구한다
0부터 15에 해당하는 문자열을 dict로 미리 정의

"""

class Solution:
    def toHex(self, num: int) -> str:
        hexdecimal = {0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'a',11:'b',12:'c',13:'d',14:'e',15:'f'}
        res = ""
        if num < 0 :
            num = 2 ** 32 + num
        elif num == 0 :
            return '0'
        while num > 0 :
            div, mod = divmod(num, 16)
            res = hexdecimal[mod] + res
            num = div
        return res