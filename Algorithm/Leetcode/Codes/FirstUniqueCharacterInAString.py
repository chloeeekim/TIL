"""

387. First Unique Character in a String : https://leetcode.com/problems/first-unique-character-in-a-string/

문자열이 주어졌을 때, 문자열 내에 한 번만 등장하는 character의 인덱스를 찾는 문제
- unique한 문자가 존재하지 않는다면 -1을 리턴

Example:
- Input : "leetcode"
- Output : 0

- Input : "loveleetcode"
- Output : 2

Note:
seen이라는 dict를 사용하여 문자열 내에서 특정 문자가 몇 번 등장하는지 확인
만약 1번만 등장한 문자가 있다면 해당 문자의 인덱스를 리턴

"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = {}
        for ch in s :
            if ch in seen :
                seen[ch] += 1
            else :
                seen[ch] = 1
        for ch in seen :
            if seen[ch] == 1 :
                return s.index(ch)
        return -1