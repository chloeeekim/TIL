"""

258. Add Digits : https://leetcode.com/problems/add-digits/

음수가 아닌 정수 num이 주어졌을 때,
한 자리수가 될 때까지 각 자릿수의 합을 구하는 일을 반복했을 때 값을 구하는 문제

Example:
- Input : 38
- Output : 2
- 3 + 8 = 11 / 1 + 1 = 2

Note:
loop나 recursion 없이 O(1) 시간에 해결할 수 있는 방법?

"""

class Solution:
    def addDigits(self, num: int) -> int:
        while True :
            nxt = 0
            while num != 0 :
                nxt += num % 10
                num //= 10
            if nxt // 10 == 0 :
                return nxt
            num = nxt