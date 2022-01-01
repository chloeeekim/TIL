"""

139. Word Break : https://leetcode.com/problems/word-break/

wordDict와 문자열 s가 주어졌을 때, wordDict 내의 문자열의 집합으로 나눌 수 있는지 확인하는 문제
- wordDict 내의 문자열은 여러 번 사용되어도 된다
- wordDict 내의 모든 문자열은 unique하다
- s와 wordDict는 오로지 알파벳 소문자로만 이루어져 있다

Example:
- Input : s = "leetcode", wordDict = ["leet","code"]
- Output : true
- "leet code"

- Input : s = "applepenapple", wordDict = ["apple","pen"]
- Output : true
- endWord인 "apple pen apple"

- Input : s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
- Output : False

Note:
bottom-up dp 방식으로 해결
recursive하게 해결하려 시도했으나 time limit으로 인해 dp로 방식 변경

"""

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        wordDict = set(wordDict)
        dp = [True] + [False] * n
        for j in range(1, n+1):
            for i in range(j):
                if dp[i] and s[i:j] in wordDict:
                    dp[j] = True
                    break
        return dp[-1]