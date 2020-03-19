"""

263. Ugly Number : https://leetcode.com/problems/ugly-number/

숫자 하나가 주어졌을 때, 해당 숫자가 Ugly Number인지 확인하는 문제
- Ugly Number는 양의 정수로, prime factor가 2, 3, 5로만 이루어진 숫자를 의미한다

Example:
- Input : 6
- Output : True
- 6 = 2 X 3

- Input : 8
- Output : True
- 8 = 2 X 2 X 2

- Input : 14
- Output : False
- 14 = 2 X 7

Note:
주어진 숫자를 2, 3, 5로 나눠주며 완전히 나눠 떨어지는지 확인하는 방식
divide() 함수에서 특정 값으로 계속 나누는 작업을 진행

"""

class Solution:
    def isUgly(self, num: int) -> bool:
        def divide(self, num: int, factor: int) -> int :
            while True :
                div, mod = divmod(num, factor)
                if mod == 0 :
                    num = div
                else :
                    return num
        if num <= 0 :
            return False
        factors = [2, 3, 5]
        for factor in factors :
            num = divide(self, num, factor)
            if num in [1] + factors :
                return True
        return False