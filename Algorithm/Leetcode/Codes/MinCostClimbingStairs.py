"""

746. Min Cost Climbing Stairs : https://leetcode.com/problems/min-cost-climbing-stairs/

각 계단 칸의 cost가 주어졌을 때, 계단을 오를 수 있는 가장 적은 cost의 합을 구하는 문제
- 한 번에 한 칸 혹은 두 칸씩만 움직일 수 있다
- 시작하는 인덱스도 0 혹은 1부터 시작할 수 있다
- cost는 [2,1000] 범위의 길이로 주어진다
- 모든 cost[i] 값은 [0, 999] 범위이다

Example:
- Input : [10,15,20]
- Output : 15
- cost[1]로 바로 이동하는 경우

- Input : [1,100,1,1,1,100,1,1,100,1]
- Output : 6
- cost[0]로 시작하여 cost[3]을 제외한 나머지 1로 이루어진 계단만 이용

Note:
한 칸 혹은 두 칸씩 움직일 수 있으므로
i-1과 i-2에 도달할 수 있는 최소 cost에 현재 칸의 cost를 더하여
현재 칸까지 이동하는 최소 cost를 구할 수 있다

"""

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        mincost = [0 for _ in range(len(cost) + 2)]
        for i in range(2, len(cost) + 2) :
            mincost[i] = min(mincost[i-1], mincost[i-2]) + cost[i-2]
        return min(mincost[-1], mincost[-2])