"""

389. Find the Difference : https://leetcode.com/problems/find-the-difference/

문자열 s와 t가 주어졌을 때, t에 추가된 문자가 무엇인지 찾는 문제
- t는 s를 랜덤하게 섞은 다음 하나의 글자가 랜덤한 위치에 추가된 문자열이다

Example:
- Input : s = "abcd", t = "abcde"
- Output : e

Note:
두 문자열을 정렬하여 비교하는 방식
s 문자열의 길이만큼 확인하여 없는 경우 t의 마지막 글자가 추가된 글자

"""

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s, t = sorted(s), sorted(t)
        for i in range(len(s)) :
            if s[i] != t[i] :
                return t[i]
        return t[-1]