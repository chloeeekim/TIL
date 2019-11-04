"""

392. Is Subsequence : https://leetcode.com/problems/is-subsequence/

두 개의 문자열 s, t가 주어졌을 때, s가 t의 subsequence인지 판별하는 문제
- t는 매우 긴 문자열(~= 500,000)이 될 수 있다
- s는 짧은 문자열(<= 100)이다
- subsequence란 원 문자열에서 몇 개의 문자를 삭제했을 때 동일한 문자열이 되는 경우이다
- 문자들의 상대적인 순서는 동일해야 한다 (ie. "ace"는 "abcde"의 subsequence이지만, "aec"는 아니다)

Example:
- Input : s = "abc", t = "ahbgdc"
- Output : true

- Input : s = "axc", t = "ahbgdc"
- Output : false

Note:
t의 문자를 하나씩 확인하면서 s와 동일한 순서로 배열된 문자가 있는 경우를 확인
s가 ""인 경우, 모든 t에 대하여 subsequence가 되므로 True를 리턴

"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s :
            return True
        idx = 0
        for ch in t :
            if s[idx] == ch :
                idx += 1
            if idx == len(s) :
                return True
        return False