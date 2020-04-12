"""

1046. Last Stone Weight : https://leetcode.com/problems/last-stone-weight/

돌의 무게가 리스트로 주어졌을 때, 아래의 조건에 따라 돌을 제거하여 얻을 수 있는 값을 구하는 문제
- 매 턴마다 가장 무거운 돌 두 개를 선택한다
- 두 돌의 무게가 동일한 경우, 둘 모두 삭제한다
- 두 돌의 무게가 다른 경우, y-x(if y>x)를 새로운 무게로 추가한다
- 위 과정을 최대 1개의 돌이 남는 경우까지 반복하여 마지막에 남는 돌의 무게를 리턴한다
- 만약 돌이 하나도 남지 않는 경우에는 0을 리턴한다

Example:
- Input : [2,7,4,1,8,1]
- Output : 1
- [2,4,1,1,1] -> [2,1,1,1] -> [1,1,1] -> [1]

Note:
heapq 모듈을 사용하여 해결
heapq는 기본적으로 min heap을 제공하므로, 돌의 무게에 -1을 곱하여 max heap으로 사용

"""

from heapq import heappush, heappop, heapify

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-1*stone for stone in stones]
        heapify(heap)
        while len(heap) > 1:
            x, y = heappop(heap), heappop(heap)
            if x != y:
                heappush(heap, x-y)
        return -heap[0] if heap else 0