"""

441. Arranging Coins : https://leetcode.com/problems/arranging-coins/

동전의 갯수 n이 주어졌을 때, 1씩 늘어나는 형태로 동전을 배열하는 경우 채울 수 있는 row의 갯수를 구하는 문제
- k번째 row는 k개의 동전으로 이루어진다
- n은 음수가 아닌 정수이며, 32-bit signed integer 범위이다

Example:
- Input : 5
- Output : 2
- 1 + 2 + 2 (3번째 row를 채우지 못함)

- Input : 8
- Output : 3
- 1 + 2 + 3 + 2 (4번째 row를 채우지 못함)

Note:
몇 번째 row에서 동전이 모자라는지를 확인
참고) 더 빠르게 해결하는 방법?

"""

class Solution:
    def arrangeCoins(self, n: int) -> int:
        i = 1
        while n >= i :
            n -= i
            i += 1
        return i - 1