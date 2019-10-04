"""

28. Implement strStr() : https://leetcode.com/problems/implement-strstr/

두 개의 문자열(haystack, needle)이 주어졌을 때,
haystack 내에서 needle이 처음 등장하는 인덱스를 리턴하는 문제
- needle이 haystack 내에 존재하지 않는다면 -1을 리턴

Example:
- Input : haystack = "hello", needle = "ll"
- Output : 2

- Input : haystack = "aaaaa", needle = "bba"
- Output : -1

Note:
find : 찾는 문자나 문자열이 없다면 -1을 리턴
index : 찾는 문자나 문자열이 없다면 오류 발생

"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)