"""

472. Concatenated Words : https://leetcode.com/problems/concatenated-words/

중복이 없는 문자열들이 포함된 words가 주어졌을 때, 모든 concatenated word를 구하는 문제
- concatenated word는 다른 2개 이상의 짧은 문자열을 합쳐서 만들어지는 문자열을 의미한다
- words 내의 문자열은 오직 알파벳 소문자로만 이루어진다
- 문자열의 길이는 0 이상 1000 이하이다

Example:
- Input : words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
- Output : ["catsdogcats","dogcatsdog","ratcatdogcat"]

- Input : words = ["cat","dog","catdog"]
- Output : ["catdog"]

Note:
check() 함수를 생성하여 각 문자열마다 concatenated word인지 dp 방식으로 확인하는 방법
참고) 더 효율적인 방법?

"""

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words = set(words)
        def check(word):
            dp = [0] * (len(word)+1)
            dp[0], l = 1, len(word)
            for i in range(l+1):
                if dp[i] == 0:
                    continue
                for j in range(i+1, l+1):                    
                    if word[i:j] in words:
                        dp[j] += dp[i]+1
            return dp[-1] >= 3
        res = []
        for word in words:
            if check(word):
                res.append(word)
        return res