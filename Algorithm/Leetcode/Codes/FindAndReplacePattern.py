"""

890. Find and Replace Pattern : https://leetcode.com/problems/find-and-replace-pattern/

문자열이 포함된 리스트 words와 pattern이 주어졌을 때, 패턴과 매치되는 문자열을 모두 찾는 문제
- 패턴과 매치된다는 것은 등장하는 문자들이 다른 문자로 맵핑되었을 때, 동일한 순서로 나열되는 경우
- 두 종류의 다른 문자가 하나의 문자로 맵핑되는 경우는 없다
- 하나의 문자가 자기 자신으로 맵핑되는 경우는 존재한다
- 주어지는 words 내의 문자열과 pattern의 길이는 동일하다
- 주어지는 모든 문자열은 알파벳 소문자이다

Example:
- Input : words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
- Output : ["mee","aqq"]

- Input : words = ["a","b","c"], pattern = "a"
- Output : ["a","b","c"]

Note:
205번 Isomorphic Strings 참고
문자열을 나타나는 순서에 따라 숫자로 변환한 문자열을 리턴하는 change()라는 함수를 만들어서 해결
두 문자열의 change()의 결과가 동일하다면 패턴이 동일하다

"""

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def change(self, string: str) -> str:
            seen = {}
            res = ""
            count = 0
            for ch in string:
                if ch in seen:
                    res += seen[ch]
                else:
                    res += str(count)
                    seen[ch] = str(count)
                    count += 1
            return res
        res, pnew = [], change(self, pattern)
        for word in words:
            if change(self, word) == pnew:
                res.append(word)
        return res