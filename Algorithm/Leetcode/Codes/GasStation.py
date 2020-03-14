"""

134. Gas Station : https://leetcode.com/problems/gas-station/

gas staion에서 채울 수 있는 연료의 양과 다음 station으로 이동하는 데 소요되는 cost가 주어졌을 때,
한 바퀴를 돌아올 수 있는 시작 지점을 구하는 문제
- 인덱스가 증가하는 방향으로 순회한다
- 조건을 만족하는 시작점이 없는 경우 -1을 리턴
- 조건을 만족하는 시작점이 있는 경우, 무조건 하나임이 보장된다
- 각 입력 리스트는 비어있지 않으며, 동일한 길이를 지니고, 음수가 포함되지 않는다

Example:
- Input : gas = [1,2,3,4,5], cost = [3,4,5,1,2]
- Output : 3

- Input : gas = [2,3,4], cost = [3,4,3]
- Output : -1

Note:
해당 인덱스에서 다음 station으로 이동하는 데 소모되거나 추가되는 연료의 양은 gas[i] - cost[i]
그 합이 음수라면 절대 시작점으로 돌아갈 수 없다
정답이 존재하는 경우 하나임이 보장되므로, 전체 사이클을 다 확인하지 않더라도 정답임을 확인할 수 있다

"""

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        length = len(gas)
        arr = [gas[i] - cost[i] for i in range(length)]
        if sum(arr) < 0 :
            return -1
        inc, res = 0, length
        for i in range(length) :
            inc += arr[i]
            if inc < 0 :
                inc = 0
                res = length
            else :
                res = min(res, i)
        return res