"""

709. To Lower Case : https://leetcode.com/problems/to-lower-case/

string이 하나 주어졌을 때, 이를 lowercase로 변환한 문자열을 구하는 문제

Example:
- Input : "Hello"
- Output : "hello"

- Input : "here"
- Output : "here"

- Input : "LOVELY"
- Output : "lovely"

Note:
ord(ch) : ascii 코드값을 반환
chr(int) : 해당 ascii 코드값의 문자를 반환
파이썬은 내장 함수로 str.lower()을 지원하므로 해당 함수를 사용해도 됨
참고) 알파벳만 포함되어 있다는 언급이 없음

"""

class Solution:
    def toLowerCase(self, str: str) -> str:
        res = ""
        for ch in str :
            asc = ord(ch)
            if asc >= 65 and asc <= 90 :
                res += chr(ord(ch) + 32)
            else :
                res += ch
        return res