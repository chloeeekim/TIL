"""

374. Guess Number Higher or Lower : https://leetcode.com/problems/guess-number-higher-or-lower/

1부터 n까지의 숫자 중 상대방이 pick한 숫자를 guess하는 문제
- pre-defined API인 guess(int num)을 사용한다
- guess() 함수는 -1(더 작은 숫자), 1(더 큰 숫자), 0(바로 그 숫자)을 리턴한다

Example:
- Input : n = 10, pick = 6
- Output : 6

Note:
binary search 형식으로 guess 함수를 호출

"""

# The guess API is already defined for you.
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        bottom, top = 1, n
        while True :            
            guessnum = (bottom + top) // 2
            res = guess(guessnum)
            if res == 0 :
                return guessnum
            elif res == 1 :
                bottom = guessnum + 1
            else :
                top = guessnum - 1