"""

69. Sqrt(x) : https://leetcode.com/problems/sqrtx/

양의 정수가 하나 주어졌을 때, 해당 정수의 제곱근을 구하는 문제
- 정수 형태로 출력한다 (소수점 아래로는 내림)

Example:
- Input : 4
- Output : 2

- Input : 8
- Output : 2
- 8의 제곱근은 2.82842...

Note:
참고) binary search로 풀어볼 것

"""

class Solution:
    def mySqrt(self, x: int) -> int:
        return int(x ** 0.5)