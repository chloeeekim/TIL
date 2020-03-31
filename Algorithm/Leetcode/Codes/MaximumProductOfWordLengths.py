"""

318. Maximum Product of Word Lengths : https://leetcode.com/problems/maximum-product-of-word-lengths/

단어로 이루어진 array가 주어졌을 때, 두 단어의 길이의 곱으로 만들 수 있는 가장 큰 값을 구하는 문제
- 선택된 두 단어는 공통된 문자가 포함되지 않아야 한다
- 단어는 모두 소문자 알파벳으로만 이루어져 있다
- 조건을 만족하는 두 단어가 없는 경우, 0을 리턴한다

Example:
- Input : ["abcw","baz","foo","bar","xtfn","abcdef"]
- Output : 16
- "abcw"와 "xtfn"

- Input : ["a","ab","abc","d","cd","bcd","abcd"]
- Output : 4
- "ab"와 "cd"

- Input : ["a","aa","aaa","aaaa"]
- Output : 0
- 조건을 만족하는 두 단어가 없다

Note:
단순하게 생각할 수 있는 방법으로 해결
조건에 부합하는 경우보다 값이 작은 게 분명한 경우는 확인하지 않도록 하여 불필요한 반복문을 줄이는 방향

"""

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        res = 0
        for i in range(len(words)) :
            wordi, before, leni = words[i], 0, len(words[i])
            for j in range(i + 1, len(words)) :
                wordj, lenj = words[j], len(words[j])
                if lenj <= before :
                    continue
                for ch in wordi :
                    if ch in wordj :
                        break
                else :
                    before = lenj
                    res = max(res, leni * lenj)
        return res