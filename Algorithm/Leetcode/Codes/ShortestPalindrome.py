"""

214. Shortest Palindrome : https://leetcode.com/problems/shortest-palindrome/

문자열 s가 주어졌을 때, 해당 문자열의 앞에 문자를 더해서 최소 길이의 palindrome을 만드는 문제
- 주어지는 문자열은 소문자 알파벳만으로 이루어져 있다

Example:
- Input : s = "aacecaaa"
- Output : "aaacecaaa"

- Input : s = "abcd"
- Output : "dcbabcd"

Note:
주어진 문자열의 앞에서부터 최대 길이의 palindrome을 찾고,
나머지 부분을 뒤집이서 앞에 붙이는 방식
참고) 더 효율적인 방식?

"""

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        point = 1
        for i in range(len(s), 1, -1):
            temp = s[:i]
            if temp == temp[::-1]:
                point = i
                break
        adding = s[point:]
        return adding[::-1]+s