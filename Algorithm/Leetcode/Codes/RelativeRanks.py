"""

506. Relative Ranks : https://leetcode.com/problems/relative-ranks/

점수 list가 주어졌을 때, 각 점수들을 상대적인 rank로 나타내는 문제
- 1등부터 3등까지는 각각 "Gold Medal", "Silver Medal", "Bronze Medal"로 나타낸다
- 4등부터는 각자의 등수로 나타낸다
- 주어지는 list는 전부 양의 정수만을 포함하며, 10,000을 넘지 않는다
- 각 점수들은 전부 unique함이 보장된다

Example:
- Input : [5, 4, 3, 2, 1]
- Output : ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]

Note:
heapq 모듈을 사용
max heap이 필요하여 -점수를 기준으로 정렬하며, 인덱스 값을 저장하기 위해 (-점수, 인덱스) 형태의 튜플을 heap에 push

"""

from heapq import heappop, heappush

class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        heap, res, medals = [], [0 for _ in range(len(nums))], ["Gold Medal", "Silver Medal", "Bronze Medal"]
        for idx, num in enumerate(nums):
            heappush(heap, (-num, idx))
        count = 0
        while heap:
            score = heappop(heap)
            res[score[1]] = medals[count] if count < 3 else str(count+1)
            count += 1
        return res