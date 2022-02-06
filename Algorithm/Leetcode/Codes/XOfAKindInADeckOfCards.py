"""

914. X of a Kind in a Deck of Cards : https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/

주어진 카드 덱을 그룹으로 나눌 때, 다음을 만족하는지 확인하는 문제
- X는 2 이상이다
- 각 그룹에는 정확히 X개의 카드가 포함된다
- 각 그룹에는 모두 동일한 숫자의 카드만 포함되어야 한다

Example:
- Input : deck = [1,2,3,4,4,3,2,1]
- Output : true
- [1,1],[2,2],[3,3],[4,4]로 나눌 수 있다

- Input : deck = [1,1,1,2,2,2,3,3]
- Output : false

- Input : deck = [1,1,2,2,2,2]
- Output : true

Note:
collections의 Counter를 사용하여 각 카드별 개수를 확인
카드별 개수의 최대공약수가 1이라면 조건을 만족하지 못한다
*를 사용하여 dict_values를 여러 건의 integer로 값을 넘김

"""

from collections import Counter

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        deckcount = Counter(deck)
        return math.gcd(*deckcount.values()) != 1