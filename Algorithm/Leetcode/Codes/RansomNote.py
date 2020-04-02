"""

383. Ransom Note : https://leetcode.com/problems/ransom-note/

두 개의 문자열이 주어졌을 때, 하나의 문자열이 다른 문자열을 이용하여 만들어질 수 있는지 확인하는 문제
- 주어진 문자열은 모두 소문자 알파벳만을 포함한다

Example:
- Input : ransomNote = "a", magazine = "b"
- Output : false

- Input : ransomNote = "aa", magazine = "ab"
- Output : false

- Input : ransomNote = "aa", magazine = "aab"
- Output : true

Note:
각 문자에 포함된 알파벳의 개수를 파악하여 문자열을 만들 수 있는지 확인
특정 알파벳이 없거나 개수가 모자란 경우 만들 수 없다

"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rcount, mcount = {}, {}
        for ch in ransomNote:
            rcount[ch] = rcount[ch] + 1 if ch in rcount else 1
        for ch in magazine:
            mcount[ch] = mcount[ch] + 1 if ch in mcount else 1
        for letter, count in rcount.items():
            if letter not in mcount:
                return False
            if count > mcount[letter]:
                return False
        return True