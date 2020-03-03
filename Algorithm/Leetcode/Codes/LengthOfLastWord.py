"""

58. Length of Last Word : https://leetcode.com/problems/length-of-last-word/

하나의 문자열이 주어졌을 때, 마지막 단어의 길이를 구하는 문제
- 주어진 문자열은 upper/lower-case 알파벳과 공백으로 이루어진다
- 단어란 공백을 포함하지 않는 character의 sequence
- 마지막 단어가 없는 경우, 0을 리턴

Example:
- Input : "Hello World"
- Output : 5

Note:
rstrip : 오른쪽 공백 지우기 / lstrip : 왼쪽 공백 지우기 / strip : 양쪽 공백 지우기
이 경우 마지막 단어를 찾기 위함이므로 왼쪽에 위치한 공백은 고려하지 않음

"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.rstrip().split()
        if not words :
            return 0
        return len(words[-1])