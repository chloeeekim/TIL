"""

409. Longest Palindrome : https://leetcode.com/problems/longest-palindrome/

문자열이 주어졌을 때, 해당 문자열로 만들 수 있는 가장 긴 palindrome의 길이를 구하는 문제
- 문자열에는 대소문자가 모두 포함되며, 대문자 A와 소문자 a는 다른 문자로 간주한다
- 주어지는 문자열의 길이는 1,010을 넘지 않는다

Example:
- Input : "abccccdd"
- Output : 7
- 가능한 palindrome 중 하나는 "dccaccd"

Note:
collections를 사용하여 문자열에 포함된 알파벳의 개수를 카운트
해당 문자가 짝수개 존재하는 경우 해당 길이만큼 palindrome을 만들 수 있다
해당 문자가 홀수개 존재하는 경우 하나를 제외한 짝수개만큼을 palindrome으로 만든 다음,
남는 하나를 가운데에 위치시켜 palindrome으로 만들 수 있다

"""

import collections

class Solution:
    def longestPalindrome(self, s: str) -> int:
        count, length, isOdd = collections.Counter(s), 0, False
        for c in count.values():
            if c % 2 == 0:
                length += c
            else:
                length += c - 1
                isOdd = True
        return length + 1 if isOdd else length