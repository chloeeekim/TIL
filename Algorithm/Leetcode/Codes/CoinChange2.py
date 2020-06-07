"""

518. Coin Change 2 : https://leetcode.com/problems/coin-change-2/

각기 다른 동전들과 구해야 하는 돈의 금액이 주어졌을 때, 해당 금액을 만들 수 있는 동전 조합의 가짓수를 구하는 문제
- 동전은 무한정 존재한다고 가정한다
- 어떠한 경우에도 해당 금액을 만들 수 없는 경우, 0을 리턴
- amount는 0 이상 5000 이하이며, 동전의 금액은 1 이상 5000 이하이다
- 주어지는 동전의 종류는 500가지를 넘지 않는다

Example:
- Input : amount = 5, coins = [1, 2, 5]
- Output : 4
- 5 / 2+2+1 / 2+1+1+1 / 1+1+1+1+1

- Input : amount = 3, coins = [2]
- Output : 0

- Input : amount = 10, coins = [10]
- Output : 1

Note:
DP로 해결
arr에 해당 인덱스에 해당하는 금액을 만들 수 있는 방법의 가짓수를 저장
amount에 해당하는 값을 만들 수 없다면 arr[-1]도 0으로 유지

"""

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        arr = [1] + [0]*amount
        for coin in coins:
            for i in range(coin, amount+1):
                arr[i] += arr[i-coin]
        return arr[-1]