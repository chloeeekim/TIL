"""

459. Repeated Substring Pattern : https://leetcode.com/problems/repeated-substring-pattern/

문자열이 주어졌을 때, 해당 문자열이 문자열 내의 substring의 반복으로 이루어졌는지 확인하는 문제
- 문자열은 전부 소문자 알파벳으로 이루어진다
- 문자열의 길이는 10000을 넘지 않는다

Example:
- Input : "abab"
- Output : True
- "ab"가 반복된다

- Input : "aba"
- Output : False

- Input : "abcabcabcabc"
- Output : True
- "abc"가 4번 반복된다 ("abcabc"가 두 번 반복되는 것도 마찬가지)

Note:
문자열의 시작부터 자른 substring을 반복하여 문자열을 만들 수 있는지 확인
mod가 0이 아니라면 전체 문자열을 만들 수 없다
substing을 반복하여 만든 문자열이 주어진 문자열과 동일한 경우 True
전체 문자열의 절반 길이까지 확인했으나 문자열이 만들어지지 않는 경우는 반복된다고 볼 수 없으므로 False

"""

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(len(s) // 2):
            repeat, mod = divmod(len(s), i+1)
            if mod != 0:
                continue
            if s == s[:i+1]*repeat:
                return True
        return False