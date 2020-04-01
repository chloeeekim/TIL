"""

322. Coin Change : https://leetcode.com/problems/coin-change/

각기 다른 동전들과 구해야 하는 돈의 금액이 주어졌을 때, 해당 금액을 만들 수 있는 동전의 최소 개수를 구하는 문제
- 동전은 무한정 존재한다고 가정한다
- 어떠한 경우에도 해당 금액을 만들 수 없는 경우, -1을 리턴

Example:
- Input : coins = [1,2,5], amount = 11
- Output : 3
- 11 = 5 + 5 + 1

- Input : coins = [2], amount = 3
- Output : -1

Note:
DP로 해결
arr에 해당 금액을 만드는 데 필요한 동전의 최소 개수를 저장하는 방식

"""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        arr = [0] + [sys.maxsize for _ in range(amount)]
        for coin in coins :
            for i in range(coin, amount + 1) :
                arr[i] = min(arr[i], arr[i - coin] + 1)
        return arr[-1] if arr[-1] != sys.maxsize else -1