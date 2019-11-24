"""

482. License Key Formatting : https://leetcode.com/problems/license-key-formatting/

주어진 문자열 S를 특정한 조건에 맞춰 형식을 변환하는 문제
- S는 alphanumeric character와 dash로만 이루어져 있다
- 문자열은 N+1개의 그룹이 N개의 dash로 나누어져야 한다
- 각 그룹은 정확하게 K개의 character가 포함되어야 하며, 첫 번째 그룹은 K보다 작을 수 있지만, 1개 이상의 문자가 포함되어야 한다
- lowercase 문자는 모두 uppercase로 변환하여 출력하여야 한다

Example:
- Input : S = "5F3Z-2e-9-w", K = 4
- Output : "5F3Z-2E9W"

- Input : S = "2-5g-3-J", K = 2
- Output : "2-5G-3J"

Note:
dash를 전부 없애고, 전부 uppercase로 변환한 문자열 생성
해당 문자열을 뒤에서부터 체크하여 K개씩 나누어 결과 문자열의 앞에 붙이는 방법

"""

class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        temp, res = S.replace('-','').upper(), ""
        if K >= len(S) :
            return temp
        for i in range(len(temp), -1, -K) :
            if i <= K :
                return temp[:i] + res
            res = '-' + temp[i-K:i] + res