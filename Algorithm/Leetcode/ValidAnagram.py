"""

242. Valid Anagram : https://leetcode.com/problems/valid-anagram/

주어진 두 문자열이 anagram인지 확인하는 문제
- 문자열에 포함된 문자는 모두 lowercase alphabet으로 이루어져 있다

Example:
- Input : s = "anagram", t = "nagaram"
- Output : true

- Input : s = "rat", t = "car"
- Output : false

Note:
두 문자열의 길이가 다르면 anagram일 수가 없음
각각의 문자열을 정렬하여 비교하는 방법 사용

"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) :
            return False
        return sorted(s) == sorted(t)