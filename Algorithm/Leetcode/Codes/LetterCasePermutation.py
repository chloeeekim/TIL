"""

784. Letter Case Permutation : https://leetcode.com/problems/letter-case-permutation/

하나의 문자열이 주어졌을 때, 알파벳의 대소문자 조합으로 만들어질 수 있는 모든 문자열을 구하는 문제
- S는 1부터 12까지의 길이로 주어진다
- S는 알파벳과 숫자로만 이루어진다

Example:
- Input : S = "a1b2"
- Output : ["a1b2","a1B2","A1b2","A1B2"]

- Input : S = "3z4"
- Output : ["3z4","3Z4"]

- Input : S = "12345"
- Output : ["12345"]

Note:
solve() 함수를 생성하여 recursive하게 해결
숫자인 경우 그대로 문자열에 붙이고, 알파벳인 경우 대문자와 소문자 두 가지로 구분
만약 S가 전부 숫자로 이루어진 경우, 가능한 경우는 자기 자신밖에 존재하지 않는다

"""

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        res = []
        def solve(self, temp: str, remain: str) :
            if not remain :
                res.append(temp)
                return
            ch, remain = remain[0], remain[1:]
            if ch.isalpha() :
                solve(self, temp + ch.lower(), remain)
                solve(self, temp + ch.upper(), remain)
            else :
                solve(self, temp + ch, remain)
        if S.isdigit() :
            res.append(S)
        else :
            solve(self, "", S)
        return res