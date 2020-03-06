"""

122. Best Time to Buy and Sell Stock II : https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

어떤 물건의 매일 변화하는 가격이 리스트로 주어졌을 때, 얻을 수 있는 가장 큰 이득을 구하는 문제
- 여러 번 물건을 사고 팔 수 있다
- 물건을 사기 전까지는 팔 수 없으며, 산 물건을 팔기 전까지는 다시 물건을 살 수 없다

Example:
- Input : [7,1,5,3,6,4]
- Output : 7
- 2일째 구입하여 3일째 판매, 4일째 구입하여 5일째 판매

- Input : [1,2,3,4,5]
- Output : 4
- 1일째 구입하여 5일째 판매. 팔기 전까지 다시 살 수 없으므로, 중간에 팔고 다시 구매하더라도 동일한 이득

- Input : [7,6,4,3,1]
- Output : 0
- 거래가 이루어지지 않으므로, 최대 이득은 0이다

Note:
부분감소수열의 가장 마지막 값(작은 값)에서 구매하여 부분증가수열의 가장 마지막 값(큰 값)에서 판매하는 것이 무조건 최대 이득
이전 이후 값을 비교하여 증가하는 값인지 감소하는 값인지를 판단
마지막 값은 파는 게 이득일 경우 무조건 판매

"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices :
            return 0
        res, buy = 0, prices[0]
        for i in range(len(prices) - 1) :
            if prices[i] > prices[i+1] :
                res += prices[i] - buy
                buy = prices[i+1]
            elif prices[i] < prices[i+1] :
                buy = min(buy, prices[i])
        if prices[-1] > buy :
            res += prices[-1] - buy
        return res