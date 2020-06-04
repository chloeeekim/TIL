"""

541. Reverse String II : https://leetcode.com/problems/reverse-string-ii/

문자열과 정수 k가 주어졌을 때, k개만큼의 문자열은 뒤집고, k개만큼은 유지하는 방식으로 2k개의 문자마다 반복하여 새로운 문자열을 구하는 문제
- 주어지는 문자열은 소문자 알파벳만 포함한다
- 주어지는 문자열의 길이와 k는 1 이상 10000 이하이다

Example:
- Input : s = "abcdefg", k = 2
- Output : "bacdfeg"

Note:
2k개의 문자를 기준으로 앞의 k개의 문자만 reverse하는 방법
reversed 함수를 사용하기 위해 문자열을 리스트로 변경한 후, 마지막에 join을 사용하여 문자열로 리턴

"""

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        slist = list(s)
        for i in range(0, len(s), 2*k):
            slist[i:i+k] = reversed(slist[i:i+k])
        return ''.join(slist)