""

942. DI String Match : https://leetcode.com/problems/di-string-match/

D와 I로 이루어진 문자열 s가 주어졌을 때, 이로 만들어낼 수 있는 permutation을 구하는 문제
- s[i]가 'I'라면 perm[i] < perm[i+1]을 의미한다
- s[i]가 'D'라면 perm[i] > perm[i+1]을 의미한다
- 문자열은 D와 I로만 이루어진다
- 여러 개의 valid한 permutation이 가능한 경우, 그 중 어느 것을 리턴해도 상관없다

Example:
- Input : s = "IDID"
- Output : [0,4,1,3,2]

- Input : s = "III"
- Output : [0,1,2,3][0,1,2,3]

- Input : s = "DDI"
- Output : [3,2,0,1]

Note:
two-pointer를 사용하여 해결

"""

class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        pmin, pmax, res = 0, len(s), []
        for ch in s:
            if ch == 'D':
                res.append(pmax)
                pmax -= 1
            else:
                res.append(pmin)
                pmin += 1
        res.append(pmax)
        return res