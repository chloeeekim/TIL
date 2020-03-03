"""

20. Valid Parentheses : https://leetcode.com/problems/valid-parentheses/

주어진 문자열의 괄호가 유효한지 확인하는 문제
- 문자열은 6가지 종류의 문자를 포함 : '(', '), '{', '}', '[', ']'
- 열리는 괄호는 반드시 같은 종류의 닫히는 괄호로 닫혀야 한다
- 열린 괄호는 반드시 정확한 순서대로 닫혀야 한다

Example:
- Input : "()"
- Output : true

- Input : "()[]{}"
- Output : true

- Input : "(]"
- Output : false

- Input : "([)]"
- Output : false

- Input : "{[]}"
- Output : true

Note:
dict 사용 (key : 열리는 괄호 / value : 닫히는 괄호)
비어있는 sequence(리스트, 튜플 등)는 false 값을 가진다
if (not) len(seq) 대신 if (not) seq 사용 권장

"""

class Solution:
    def isValid(self, s: str) -> bool:
        p_map = {'(' : ')', '{' : '}', '[' : ']'}
        stack = []
        for i in s :
            if i in ['(', '{', '['] :
                stack.append(i)
            elif stack and i == p_map[stack[-1]] :
                stack.pop()
            else :
                return False
        return not stack