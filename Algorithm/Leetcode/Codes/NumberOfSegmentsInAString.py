"""

434. Number of Segments in a String : https://leetcode.com/problems/number-of-segments-in-a-string/

문자열이 주어졌을 때, 문자열이 몇 개의 segment로 구성되어 있는지 찾는 문제
- segment : 공백이 포함되지 않은 연속된 문자열
- 문자열에는 출력되지 않는(non-printable) 문자는 존재하지 않는다

Example:
- Input : "Hello, my name is John"
- Output : 5

Note:
문자열을 공백을 기준으로 list로 나누고, 해당 list의 길이를 출력하는 방식

"""

class Solution:
    def countSegments(self, s: str) -> int:
        l = s.split()
        return len(l)