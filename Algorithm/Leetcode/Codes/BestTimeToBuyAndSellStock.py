"""

121. Best Time to Buy and Sell Stock : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

어떤 물건의 매일 변화하는 가격이 리스트로 주어졌을 때, 얻을 수 있는 가장 큰 이득을 구하는 문제
- 여러 번 물건을 사고 팔 수 없다
- 물건을 사기 전까지는 팔 수 없다

Example:
- Input : [7,1,5,3,6,4]
- Output : 5
- price가 1인 2일째에 구입하여 price가 6인 5일째에 판매

- Input : [7,6,4,3,1]
- Output : 0
- 거래가 이루어지지 않으므로, 최대 이득은 0이다

Note:
이전 일자의 가장 작은 값과 현재 값의 차이가 해당 날짜에 얻을 수 있는 최대 이득이 된다

"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res, tmpmin = 0, sys.maxsize
        for price in prices :
            tmpmin = min(tmpmin, price)
            res = max(res, price - tmpmin)
        return res