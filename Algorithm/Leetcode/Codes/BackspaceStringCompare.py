"""

844. Backspace String Compare : https://leetcode.com/problems/backspace-string-compare/

두 개의 문자열이 주어졌을 때, 두 문자열이 동일한지 확인하는 문제
- '#'은 backspace character를 의미한다
- 두 문자열의 길이는 200을 넘지 않는다

Example:
- Input : S = "ab#c", T = "ad#c"
- Output : true
- 둘 다 "ac"가 된다

- Input : S = "ab##", T = "c#d#"
- Output : true
- 둘 다 ""가 된다

- Input : S = "a##c", T = "#a#c"
- Output : true
- 둘 다 "c"가 된다

- Input : S = "a#c", T = "b"
- Output : false
- S는 "c"가 되고, T는 "b"가 된다

Note:
getstr() 함수에서 backspace를 처리한 문자열을 리턴
먼저 문자를 추가했다가 backspace가 나오는 경우에 지우는 것보다,
backspace가 있었다면 문자를 넣지 않는 것이 더 효율적이므로 string을 reverse하여 뒤에서부터 확인

"""

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def getstr(string: str) -> list:
            string, res, skip = string[::-1], "", 0
            for ch in string:
                if ch == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    res += ch
            return res
        return getstr(S) == getstr(T)