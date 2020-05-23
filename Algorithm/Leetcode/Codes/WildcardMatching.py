"""

44. Wildcard Matching : https://leetcode.com/problems/wildcard-matching/

input string s와 pattern p가 주어졌을 때, wildcard가 포함된 p가 s와 매치되는지 확인하는 문제
- '?'는 any single character와 매치된다
- '*'는 any sequence of characters와 매치된다 (빈 문자열도 포함)
- s는 빈 문자열일 수 있으며, a-z까지의 영문 소문자로만 이루어진다
- p는 빈 문자열일 수 있으며, a-z까지의 영문 소문자와 ?와 *로만 이루어진다

Example:
- Input : s = "aa", p = "a"
- Output : false

- Input : s = "aa", p = "*"
- Output : true

- Input : s = "cb", p = "?a"
- Output : false

- Input : s = "adceb", p = "*a*b"
- Output : true

- Input : s = "acdcb", p = "a*c?b"
- Output : false

Note:
2차원 배열을 사용하여 dp로 해결
p가 '?'거나 s와 동일한 문자라면 이전 값(i-1, j-1)을 그대로 선택
p가 '*'가 아니면서 s와 다른 문자라면 무조건 false
p가 '*'라면 s의 문자와 상관없이 이전에 true가 된다면 무조건 true
p의 처음에 등장하는 문자가 '*'이면서 empty seqence에 매치되는 경우를 대비하여 '*'가 나오는 부분까지 arr의 초기값을 true로 변경

"""

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        arr = [[False for _ in range(len(s)+1)] for _ in range(len(p)+1)]
        arr[0][0] = True
        for i in range(len(p)):
            if p[i] != '*':
                break
            arr[i+1][0] = True
        for i in range(1, len(p)+1):
            for j in range(1, len(s)+1):
                if p[i-1] == '*':
                    arr[i][j] = arr[i-1][j] or arr[i-1][j-1] or arr[i][j-1]
                elif p[i-1] == '?' or p[i-1] == s[j-1]:
                    arr[i][j] = arr[i-1][j-1]
                else:
                    arr[i][j] = False
        return arr[-1][-1]