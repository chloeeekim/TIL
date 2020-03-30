"""

313. Super Ugly Number : https://leetcode.com/problems/super-ugly-number/

prime 리스트가 주어졌을 때, n번째 ugly number를 구하는 문제
- Ugly Number는 양의 정수로, prime factor가 주어진 prime 리스트의 값으로만 이루어진 숫자를 의미한다
- 1은 항상 ugly number이다
- priems 리스트는 증가하는 순서로 정렬되어 있다

Example:
- Input : n = 12, primes = [2,7,13,19]
- Output : 32
- ugly number: 1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32

Note:
heapq 모듈을 이용하여 min heap을 사용하여 해결
ugly number에 각 prime들을 곱한 수들 역시 ugly number가 된다

"""

from heapq import heappop, heappush

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        heap, count = [1], 0
        while count < n :
            num = heappop(heap)
            while heap and heap[0] == num :
                heappop(heap)
            count += 1
            if count == n :
                return num
            for prime in primes :
                heappush(heap, num * prime)