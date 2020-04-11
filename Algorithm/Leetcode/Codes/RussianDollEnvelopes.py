"""

354. Russian Doll Envelopes : https://leetcode.com/problems/russian-doll-envelopes/

각 봉투의 width, height pair 리스트가 주어졌을 때, Russian Doll처럼 만들 수 있는 봉투의 최대 개수를 구하는 문제
- width와 height 모두 큰 봉투 안에만 들어갈 수 있다 (같아도 들어갈 수 없다)
- 봉투를 회전하는 것은 허용하지 않는다

Example:
- Input : [[5,4],[6,4],[6,7],[2,3]]
- Output : 3
- [2,3] -> [5,4] -> [6,7]

Note:
해당 envelop 내에 들어가는 봉투의 최대 개수를 리스트에 저장하는 방식
정렬하여 작은 봉투에서 큰 봉투 순서로 순회
참고) 더 효율적인 방법? Time Limit이 계속 뜨다가 겨우 통과한 수준

"""

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0
        envelopes, count = sorted(envelopes), [0 for _ in range(len(envelopes))]
        for i in range(len(envelopes)):
            c = 0
            for j in range(i, -1, -1):
                if count[j] <= c:
                    continue
                if envelopes[j][0] < envelopes[i][0] and envelopes[j][1] < envelopes[i][1]:
                    c = count[j]
            count[i] = c+1
        return max(count)