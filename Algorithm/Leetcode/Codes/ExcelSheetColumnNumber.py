"""

171. Excel Sheet Column Number : https://leetcode.com/problems/excel-sheet-column-number/

엑셀 시트에 나타나는 것과 동일한 column title이 주어졌을 때, 이를 숫자로 변경하는 문제
- A -> 1, B -> 2, ... , Z -> 26, AA -> 27, AB -> 28 ... 과 같은 순서로 진행된다

Example:
- Input : "A"
- Output : 1

- Input : "AB"
- Output : 28

- Input : "ZY"
- Output : 701

Note:
26진법을 계산하듯이 계산
ord(ch) : 문자를 아스키 코드로 변환
chr(num) : 아스키 코드를 문자로 변환

"""

class Solution:
    def titleToNumber(self, s: str) -> int:
        res = 0
        for ch in s :
            res *= 26
            res += (ord(ch) - ord('A') + 1)
        return res