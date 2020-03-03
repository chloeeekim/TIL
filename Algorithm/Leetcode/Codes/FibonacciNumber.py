"""

509. Fibonacci Number : https://leetcode.com/problems/fibonacci-number/

정수 N이 주어졌을 때, N번째 피보나치 수를 찾는 문제
- 피보나치 수는 다음과 같은 조건을 만족하는 수열이다
- F(0) = 0, F(1) = 1, F(N) = F(N-1) + F(N-2), for N > 1

Example:
- Input : 2
- Output : 1
- F(2) = F(1) + F(0) = 1 + 0 = 1

- Input : 3
- Output : 2
- F(3) = F(2) + F(1) = 1 + 1 = 2

- Input : 4
- Output : 3
- F(4) = F(3) + F(2) = 2 + 1 = 3

Note:
- Solution 1
recursive하게 구하는 방법
이전에 구한 값들이 저장되지 않기 때문에 속도가 느리고, 메모리 측면에서도 비효율적
- Solution 2
이전에 구한 값들을 배열(리스트)에 저장하는 방법
메모리 측면에서도 효율적이며 동일한 값을 여러 번 구할 필요가 없으므로 속도가 빠르다

"""

# Solution 1
class Solution:
    def fib(self, N: int) -> int:
        if N == 0 :
            return 0
        elif N == 1 :
            return 1
        else :
            return self.fib(N-1) + self.fib(N-2)

# Solution 2
class Solution:
    def fib(self, N: int) -> int:
        fibonacci = [0, 1]
        for i in range(2, N + 1) :
            fibonacci.append(fibonacci[-1] + fibonacci[-2])
        return fibonacci[N]