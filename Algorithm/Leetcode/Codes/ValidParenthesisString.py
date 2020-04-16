"""

678. Valid Parentheses String : https://leetcode.com/problems/valid-parentheses-string/

주어진 문자열의 괄호가 유효한지 확인하는 문제
- 문자열은 3가지 종류의 문자를 포함 : '(', ')', '*'
- 열리는 괄호는 반드시 닫히는 괄호로 앞에 있어야 한다
- '*'는 ')', '(' 혹은 empty string이 될 수 있다
- 빈 문자열 역시 valid하다

Example:
- Input : "()"
- Output : true

- Input : "(*)"
- Output : true

- Input : "(*))"
- Output : true

Note:
여는 괄호, 닫는 괄호를 각각 +1, -1로 간주할 때,
low는 가능한 가장 작은 값이 되고, high는 가능한 가장 큰 값이 된다
high가 0보다 작아지면 valid하지 않다

"""

class Solution:
    def checkValidString(self, s: str) -> bool:
        low, high = 0, 0
        for ch in s:
            low += 1 if ch == '(' else -1
            high += 1 if ch != ')' else -1
            if high < 0:
                return False
            low = max(low, 0)
        return low == 0