"""

290. Word Pattern : https://leetcode.com/problems/word-pattern/

pattern과 string이 주어졌을 때, 주어진 string이 pattern에 맞게 구성되어 있는지를 확인하는 문제
- pattern은 소문자 알파벳으로만 이루어진다
- string은 소문자 알파벳으로 이루어져 있으며, single space로 구분된다

Example:
- Input : pattern = "abba", str = "dog cat cat dog"
- Output : true

- Input : pattern = "abba", str = "dog cat cat fish"
- Output : false

- Input : pattern = "aaaa", str = "dog cat cat dog"
- Output : false

- Input : pattern = "abba", str = "dog dog dog dog"
- Output : false

Note:
dict를 사용하여 해결
pattern과 word를 key, value의 쌍으로 저장

"""

class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        words, pat = str.split(), {}
        if len(pattern) != len(words) :
            return False
        for i, ch in enumerate(pattern):
            if ch not in pat :
                if words[i] in pat.values() :
                    return False
                pat[ch] = words[i]
            else :
                if words[i] != pat[ch] :
                    return False
        return True