"""

575. Distribute Candies : https://leetcode.com/problems/distribute-candies/

n개의 캔디의 타입이 주어졌을 때, n/2개의 캔디만 먹을 수 있는 경우, 먹을 수 있는 가장 많은 종류의 캔디를 구하는 문제
- n은 항상 짝수이다
- candies[i]는 i번째 캔디의 타입이다

Example:
- Input : candyType = [1,1,2,2,3,3]
- Output : 3
- 3개의 캔디만 먹을 수 있으므로, [1, 2, 3] 세 가지의 캔디를 선택

- Input : candyType = [1,1,2,3]
- Output : 2
- 2개의 캔디만 먹을 수 있으므로, [1, 2] 혹은 [1, 3] 혹은 [2, 3] 두 가지의 캔디를 선택

- Input : candyType = [6,6,6,6]
- Output : 1
- 2개의 캔디를 먹을 수 있으나, 무조건 [6, 6]이므로 하나의 캔디만 먹을 수 있다

Note:
캔디의 타입이 1부터 시작하거나 정렬되어 있다는 보장이 없으므로
set을 사용하여 unique한 캔디 타입의 개수를 확인
캔디 타입이 n/2를 넘는 경우 n/2개가 섭취할 수 있는 최대의 캔디이므로
캔디 타입과 n//2 중 작은 값을 선택

"""


class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        unique = len(set(candies))
        return min(unique, len(candies)//2)
