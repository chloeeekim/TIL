"""

50. Pow(x,n) : https://leetcode.com/problems/powx-n/

pow(x,n) 함수를 구현하는 문제

Example:
- Input : 2.00000, 10
- Output : 1024.00000

- Input : 2.10000, 3
- Output : 9.26100

- Input : 2.00000, -2
- Output : 0.25000

Note:
n이 음수면 x 대신 1/x를 사용
n이 2의 배수인 경우 x^n = x^(n/2)이고, 2의 배수가 아닌 경우 x^n = x*x^(n/2)

"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0 :
            n *= -1
            x = 1/x
        res = 1
        while n > 0 :
            if n%2 != 0 :
                res *= x
            x *= x
            n //= 2
        return res