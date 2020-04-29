"""

796. Rotate String : https://leetcode.com/problems/rotate-string/

문자열 A, B가 주어졌을 때, A를 shift하여 B가 만들어질 수 있는지를 확인하는 문제
- A와 B의 길이는 최대 100이다

Example:
- Input : A = 'abcde', B = 'cdeab'
- Output : true

- Input : A = 'abcde', B = 'abced'
- Output : false

Note:
isrotate() 함수를 생성하여 B를 해당 인덱스로부터 시작했을 때 A와 동일하게 만들어지는지 확인
A를 기준으로 하여 B의 인덱스 계산만 진행

"""

class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        alen = len(A) if A else 0
        blen = len(B) if B else 0
        if alen != blen :
            return False
        if A == B:
            return True
        def isrotate(bidx: int, blen: int) -> bool:
            for i, ch in enumerate(A):
                if A[i] != B[bidx]:
                    return False
                bidx = bidx+1 if bidx < blen-1 else 0
            return True
        for i, ch in enumerate(B):
            if ch == A[0]:
                res = isrotate(i, blen)
                if res:
                    return True
        return False