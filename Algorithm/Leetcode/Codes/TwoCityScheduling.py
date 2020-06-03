"""

1029. Two City Scheduling : https://leetcode.com/problems/two-city-scheduling/

2N명의 사람들이 A 도시와 B 도시로 가는 데 드는 cost가 주어졌을 때, 각 도시로 N명의 사람이 가는 최소한의 cost를 구하는 문제
- costs의 길이는 1 이상 100 이하인 짝수임이 보장된다
- 각 도시로 가는 cost는 1 이상 1000 이하이다

Example:
- Input : [[10,20],[30,200],[400,50],[30,20]]
- Output : 110
- 10 (첫 번째 사람 -> A) + 30 (두 번째 사람 -> A) + 50 (세 번째 사람 -> B) + 20 (네 번째 사람 -> D)

Note:
A 도시로 가는 것과 B 도시로 가는 것의 cost 차이가 큰 경우 작은 쪽을 선택하는 것이 유리
모두가 A 도시로 갈 때의 전체 cost의 합에서 B 도시로 가는 것이 유리한 사람들을 절반을 구해 cost를 빼주는 방식

"""

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        totalA = sum(cost for cost, _ in costs)
        diff = [b-a for a, b in costs]
        diff = sum(sorted(diff)[:len(costs)//2])
        return totalA+diff