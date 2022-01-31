"""

1672. Richest Customer Wealth : https://leetcode.com/problems/richest-customer-wealth/

각 사람의 계좌 정보가 리스트의 형태로 주어졌을 때, 가장 부유한 사람의 총 자산을 구하는 문제

Example:
- Input : accounts = [[1,2,3],[3,2,1]]
- Output : 6

- Input : accounts = [[1,5],[7,3],[3,5]]
- Output : 10

- Input : accounts = [[2,8,7],[7,1,3],[1,9,5]]
- Output : 17

Note:
max 값과 sum을 비교

"""

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maximum = 0
        for account in accounts:
            maximum = max(maximum, sum(account))
        return maximum