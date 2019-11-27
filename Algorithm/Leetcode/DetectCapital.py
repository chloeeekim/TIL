"""

520. Detect Capital : https://leetcode.com/problems/detect-capital/

문자열 word가 주어졌을 때, 특정 형태인지 확인하는 문제
- 모든 문자가 대문자로 주어지는 경우 (ex. "USA")
- 모든 문자가 소문자로 주어지는 경우 (ex. "leetcode")
- 첫 글자만 대문자로 주어지는 경우 (ex. "Google")

Example:
- Input : "USA"
- Output : true

- Input : "FlaG"
- Output : False

Note:
isupper() : 모든 문자가 대문자인지 확인
islower() : 모든 문자가 소문자인지 확인
istitle() : 첫 글자만 대문자이고 나머지 문자가 소문자인지 확인

"""

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.isupper() or word.islower() or word.istitle()