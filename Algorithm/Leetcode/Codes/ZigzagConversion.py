"""

6. Zigzag Conversion : https://leetcode.com/problems/zigzag-conversion/

문자열과 row가 주어졌을 때, 지그재그 형태로 놓은 경우의 순서로 재구성하는 문제
- 문자열은 알파벳(대소문자), ',', '.'으로 이루어져 있다
- row는 1 이상 1000 이하이다

Example:
- Input : s = "PAYPALISHIRING", numRows = 3
- Output : "PAHNAPLSIIGYIR"
-
P   A   H   N
A P L S I I G
Y   I   R

- Input : s = "PAYPALISHIRING", numRows = 4
- Output : "PINALSIGYAHRPI"
-
P     I    N
A   L S  I G
Y A   H R
P     I

- Input : s = "A", numRows = 1
- Output : "A"

Note:
문자를 순서대로 ans[i] 리스트에 추가하여 마지막에 합치는 방식으로 해결
numRows가 1인 경우 문자열이 변하지 않으므로 해당 문자열을 그대로 반환

"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        ans, i, isup = ["" for i in range(numRows)], 0, True
        for ch in s:
            ans[i] += ch
            if isup:
                i += 1
                if i == numRows:
                    isup = False
                    i -= 2
            else:
                i -= 1
                if i == -1:
                    isup = True
                    i += 2
        ansstr = "".join(ans)
        return ansstr