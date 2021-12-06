"""

394. Decode String : https://leetcode.com/problems/decode-string/

encoded된 주어진 문자열을 decode하는 문제
- k[encoded_string]은 encoded_string이 k번 반복되는 것을 의미한다
- k는 양수임이 보장된다
- 알파벳과 숫자는 혼용되어 사용되지 않는다. 즉, 3a 혹은 2[4] 같은 예시는 존재하지 않는다

Example:
- Input : s = "3[a]2[bc]"
- Output : "aaabcbc"

- Input : s = "3[a2[c]]"
- Output : "accaccacc"

- Input : s = "2[abc]3[cd]ef"
- Output : "abcabccdcdcdef"

- Input : s = "abc3[cd]xyz"
- Output : "abccdcdcdxyz"

Note:
stack을 사용하여 해결
']' 문자가 나타난 경우 이전에 나타난 string들을 확인하고, k번만큼 반복하여 다시 stack에 push

"""

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch == ']':
                pattern = ''
                while stack[-1] != '[':
                    pattern = stack[-1] + pattern
                    del stack[-1]
                del stack[-1]
                digit, counter = 0, 0
                while stack and stack[-1].isdigit():
                    digit += int(stack[-1]) * (10 ** counter)
                    counter += 1
                    del stack[-1]
                decoded = pattern * digit
                for c in decoded:
                    stack.append(c)
            else:
                stack.append(ch)
        return ''.join(stack)