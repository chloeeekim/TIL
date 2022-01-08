"""

516. Longest Palindromic Subsequence : https://leetcode.com/problems/longest-palindromic-subsequence/

문자열이 주어졌을 때, 해당 문자열로 만들 수 있는 가장 긴 palindromic subsequence의 길이를 구하는 문제
- subsequence란 순서는 변경하지 않은 채 포함된 문자를 지우거나 지우지 않아서 만들어지는 문자열을 의미한다
- 주어지는 문자열의 길이는 1 이상 1000 이하이다
- 문자열에는 오로지 알파벳 소문자만 포함된다

Example:
- Input : s = "bbbab"
- Output : 4
- "bbbb"가 가장 긴 palindromic subsequence이다

- Input : s = "cbbd"
- Output : 2
- "bb"가 가장 긴 palindromic subsequence이다

Note:
dp를 이용하여 해결
left와 right의 문자가 동일한 경우 palindrome으로 만들 수 있으므로 2를 더한다
left와 right가 다른 경우 왼쪽과 오른쪽 각각에서 max 값을 구한다

"""

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = {}
        def getLen(left, right):
            if left == right:
                return 1
            if left > right:
                return 0
            if (left, right) in dp:
                return dp[(left, right)]
            if s[left] == s[right]:
                dp[(left, right)] = 2+getLen(left+1, right-1)
            else:
                dp[(left, right)] = max(getLen(left+1, right), getLen(left, right-1))                
            return dp[(left, right)]
        return getLen(0, len(s)-1)
                