"""

32. Longest Valid Parentheses : https://leetcode.com/problems/longest-valid-parentheses/

'('와 ')'로만 이루어진 문자열이 주어졌을 때, longest valid parentheses substring의 길이를 구하는 문제

Example:
- Input : "(()"
- Output : 2
- longest valid parentheses substring : "()"

- Input : ")()())"
- Output : 4
- longest valid parentheses substring : "()()"

Note:
stack을 사용하여 해결
'('가 나오면 stack에 해당 인덱스를 push하는 방법으로 substring의 길이를 구함
참고) 더 나은 방법?

"""

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack, maxlen = [-1], 0
        for i in range(len(s)) :
            if s[i] == '(' :
                stack.append(i)
            else :
                pop = stack.pop(-1)
                if not stack :
                    stack.append(i)
                else :
                    maxlen = max(maxlen, i - stack[-1])
        return maxlen