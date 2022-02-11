"""

1047. Remove All Adjacent Duplicates In String : https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

소문자 알파벳으로만 이루어진 문자열 s가 주어졌을 때, 인접한 두 개의 문자가 동일한 경우 삭제하여 결과를 리턴하는 문제
- 더 이상 인접하고 동일한 문자열이 없을 때까지 반복한다

Example:
- Input : s = "abbaca"
- Output : "ca"
- "abbaca" -> "aaca" -> "ca"

- Input : s = "azxxzy"
- Output : "ay"

Note:
stack을 사용하여 해결

"""

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for ch in s:
            if stack and stack[-1] == ch:
                stack.pop()
            else:
                stack.append(ch)
        return "".join(stack)