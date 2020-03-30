"""

264. Ugly Number II : https://leetcode.com/problems/ugly-number-ii/

n번째 ugly number를 구하는 문제
- Ugly Number는 양의 정수로, prime factor가 2, 3, 5로만 이루어진 숫자를 의미한다
- 1은 항상 ugly number이다
- n은 1690을 넘지 않는다

Example:
- Input : n = 10
- Output : 12
- ugly number: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12

Note:
heapq 모듈을 이용하여 min heap을 사용하여 해결
ugly number에 2, 3, 5를 곱한 수들 역시 ugly number가 된다

"""

from heapq import heappush, heappop

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap, count, primes = [1], 0, [2, 3, 5]
        while count < n :
            num = heappop(heap)
            while heap and heap[0] == num :
                heappop(heap)
            count += 1
            if count == n :
                return num
            for prime in primes :
                heappush(heap, num * prime)