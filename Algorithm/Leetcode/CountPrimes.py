"""

204. Count Primes : https://leetcode.com/problems/count-primes/

음수가 아닌 숫자 n이 주어졌을 때, n보다 작은 숫자들 중 소수(prime number)의 갯수를 구하는 문제

Example:
- Input : 10
- Output : 4
- 10 미만의 소수는 2, 3, 5, 7

Note:
primes 리스트로 해당 인덱스의 숫자가 prime인지 아닌지를 관리
소수가 발견되는 경우 해당 숫자의 배수는 전부 소수가 아니므로 false로 변경
참고) 숫자를 하나씩 소수인지 확인해나가는 방법은 time limit에 걸림
참고) 더 빠른 방법?

"""

class Solution:
    def countPrimes(self, n: int) -> int:
        primes = [False, False] + [True] * (n - 2)
        if n < 2 :
            return 0
        count = 0
        for i in range(2, n) :
            if not primes[i] :
                continue
            count += 1
            for j in range(i * 2, n, i) :
                primes[j] = False
        return count